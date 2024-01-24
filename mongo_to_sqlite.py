import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["scrapping-database"]
collection = db["scrapy_quotes"]

conn = sqlite3.connect("scrapping_quotes.db")

query = " CREATE TABLE quotes (quote varchar(255), author varchar(100), tags varchar(100))"

cursor = conn.cursor()
cursor.execute(query)
conn.commit()

sql = "INSERT INTO quotes(quote, author, tags) VALUES (?,?,?)"
for doc in collection.find():
    # Execute INSERT statement with extracted data
    cursor.execute(sql, [doc['quote'], doc['author'],doc['tags']])
    conn.commit()

client.close()
conn.close()