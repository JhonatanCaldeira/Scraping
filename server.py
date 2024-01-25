from flask import Flask, request
import pymongo
import subprocess
import os
import json
from simplon_scrapy.simplon_scrapy import settings
from bson.json_util import dumps, loads 

app = Flask(__name__)

@app.route("/")
def home():
    return "Server UP and Running"

@app.route("/api/random_quote")
def get_random_quote():
    client = pymongo.MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DATABASE]
    collection = db[settings.SPIDERS_TABLE_QUOTE]
    
    try:
        random_document = collection.aggregate([
            {"$sample": {"size": 1}}
        ])

        return_quote = []
        for document in random_document:
            return_quote.append(document["quote"])
            return_quote.append(document["author"])
    finally:    
        client.close()

    return json.dumps(return_quote)

@app.route('/api/run_spider')
def run_spider():
    try:
        os.chdir('simplon_scrapy')
        subprocess.run(['scrapy', 'crawl', 'quotes'], check=True)
        return json.dumps("Scrapping executed successfully!")
    except subprocess.CalledProcessError:
        return "Erreur lors de l'exécution du Spider."

@app.route("/api/get_log")
def get_log():
    client = pymongo.MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DATABASE]
    collection = db[settings.SPIDERS_TABLE_LOG]
    
    try:
        logs = collection.find()
        list_logs = list(logs)
    finally:    
        client.close()

    return dumps(list_logs)