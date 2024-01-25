import streamlit as st
import requests

BASE_URL = "http://localhost:5000"
logs = requests.get(f"{BASE_URL}/api/get_log").json()
st.write(logs)
#st.table(logs)