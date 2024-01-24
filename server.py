from flask import Flask, request
import json
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/api/random_quote")
def get_one_quote():
    client = MongoClient()
    db = client['scrapping-database']
    collection = db['scrapy_quotes']

    random_document = collection.aggregate([
        {"$sample": {"size": 1}}
    ])

    return_quote = []
    for document in random_document:
        return_quote.append(document["Quote"])
        return_quote.append(document["Author"])
        
    return json.dumps(return_quote)