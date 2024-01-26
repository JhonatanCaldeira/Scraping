from flask import Flask
import pymongo
import subprocess
import os
import json
import logging
from simplon_scrapy.simplon_scrapy import settings
from bson.json_util import dumps

app = Flask(__name__)

format_string = "%(asctime)s:%(levelname)s:%(message)s"
logging.basicConfig(
    filename="flask.log", encoding="utf-8",
    level=logging.DEBUG, format=format_string
)


@app.route("/")
def home():
    """This function check Flask server status"""

    return "Server UP and Running", 200


@app.route("/api/random_quote")
def get_random_quote():
    """Function to get a random quote from the MongoDB

    Returns:
        (json): Returns a Json List in the format:
            {
                "quotes":<quotes>,
                "author":<author>
            }
    """
    return_quote = []

    try:
        client = pymongo.MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DATABASE]
        collection = db[settings.SPIDERS_TABLE_QUOTE]

        random_document = collection.aggregate([{"$sample": {"size": 1}}])

        for document in random_document:
            return_quote.append(document["quote"])
            return_quote.append(document["author"])

            logging.info(
                f"""Quote: {document["quote"]} /
                         | Author: {document["author"]}"""
            )
    except IndexError:
        logging.info("Empty Collection")
        return_quote.append("Empty collection, please release the spiders!")

        return return_quote, 400

    except Exception as e:
        logging.error(f"{str(e)}")
        raise
    finally:
        client.close()

    return json.dumps(return_quote), 200


@app.route("/api/run_spider")
def run_spider():
    """Function to execute the Spiders from Scrapy.

    Returns:
        (str): Confirmation of completition.

    Exception:
        Raise: subprocess.CalledProcessError.
    """
    try:
        os.chdir("simplon_scrapy")
        subprocess.run(["scrapy", "crawl", "quotes"], check=True)
        logging.info("Scrapping executed successfully")

        return json.dumps("Scrapping executed successfully!"), 200
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during the spider execution | {str(e)}")

        return json.dumps("Error during the spider execution."), 400


@app.route("/api/get_log")
def get_log():
    client = pymongo.MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DATABASE]
    collection = db[settings.SPIDERS_TABLE_LOG]

    try:
        logs = collection.find()
        list_logs = list(logs)
    except Exception as e:
        logging.error(f"{str(e)}")
        raise
    finally:
        client.close()

    return dumps(list_logs), 200
