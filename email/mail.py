from redmail import EmailSender
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path(__file__).parent / "config.ini")

host = (config["server"]["host"],)
port = (config["server"]["port"],)
username = (config["login"]["mail"],)
password = config["login"]["key"]

email = EmailSender(
    host=config["server"]["host"],
    port=config["server"]["port"],
    username=config["login"]["mail"],
    password=config["login"]["key"],
)

email.send(
    subject="test",
    sender=config["login"]["mail"],
    receivers=["jhonatancaldeira@yahoo.com.br"],
    text="teste",
    html="teste",
)
