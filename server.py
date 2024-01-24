from flask import Flask, request
from pymongo import MongoClient
import subprocess, os, json

app = Flask(__name__)

@app.route("/")
def home():
    return "Server UP and Running"

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
        return_quote.append(document["quote"])
        return_quote.append(document["author"])
        
    return json.dumps(return_quote)

@app.route('/api/run-spider')
def run_spider():
    try:
        # Exécuter la commande Scrapy
        os.chdir('simplon_scrapy')
        subprocess.run(['scrapy', 'crawl', 'quotes'], check=True)
        return "Spider exécuté avec succès."
    except subprocess.CalledProcessError:
        return "Erreur lors de l'exécution du Spider."