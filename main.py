import streamlit as st
import requests

BASE_URL = "http://localhost:5000"
labels = requests.get(f"{BASE_URL}/api/random_quote").json()

st.title(labels[0])
st.write(f'By {labels[1]}')