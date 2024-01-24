import scrapy
from scrapy import Request
from simplon_scrapy.items import Quotes
from scrapy.loader import ItemLoader

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = Quotes()
            item["quote"] = quote.xpath('span[@class="text"]/text()').extract_first().replace("“","").replace("”","")
            item["author"] = quote.xpath('span/small[@class="author"]/text()').extract_first()
            item["tags"] = quote.xpath('div[@class="tags"]/meta[@class="keywords"]/@content').extract_first()

            yield item

        relative_next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)


