import streamlit as st
import requests

BASE_URL = "http://localhost:5000"

spiders = st.button("Release the Spiders!!!")

if spiders:
    st.write("Spiders released!")
    result = requests.get(f"{BASE_URL}/api/run_spider").json()
    st.write(result)
