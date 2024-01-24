import streamlit as st
from pymongo import MongoClient
import pprint
import requests

BASE_URL = "http://localhost:5000"
# BASE_URL = "http://jhonatancaldeira.pythonanywhere.com"
labels = requests.get(f"{BASE_URL}/api/random_quote").json()
st.title(labels[0])
st.write(f'By {labels[1]}')