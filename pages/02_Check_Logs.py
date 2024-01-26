import streamlit as st
import requests
import configparser
from json2html import *  # noqa
from pathlib import Path
from redmail import EmailSender


BASE_URL = "http://localhost:5000"
logs = requests.get(f"{BASE_URL}/api/get_log").json()

to_email = st.text_input("Send To: ")
send = st.button("Send Log")

st.write(logs)

if send:
    config = configparser.ConfigParser()
    config.read(Path(__file__).parent / "config.ini")

    email = EmailSender(
        host=config["server"]["host"],
        port=config["server"]["port"],
        username=config["login"]["mail"],
        password=config["login"]["key"],
    )

    email.send(
        subject="[LOGS] Scrapy Quotes",
        sender=config["login"]["mail"],
        receivers=[to_email],
        html=json2html.convert(json=logs), # noqa
    )
