# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from simplon_scrapy.settings import SPIDERS_TABLE_QUOTE
import pymongo

class SimplonScrapyPipeline:
    def process_item(self, item, spider):
        return item

class MongoPipeline:
    collection_name = SPIDERS_TABLE_QUOTE

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        search = {'quote': item['quote'], 'author': item['author']}
        if not self.db[self.collection_name].find_one(search):
            self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item