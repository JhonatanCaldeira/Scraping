from flask import Flask, request
from pathlib import Path
import json
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_FILE = 'scrapping_quotes.db'
DB_PATH = ROOT_DIR / DB_FILE

app = Flask(__name__)

@app.route("/api/random_quote")
def get_one_quote():
    query = "SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    
    rows = cursor.fetchall()
    return_quote = []

    for row in rows:
        return_quote.append(row[0])
        return_quote.append(row[1])

    return json.dumps(return_quote)