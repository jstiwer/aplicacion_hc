import streamlit as st
import requests

API_URL = "https://api1-zv36.onrender.com/chat"  # Replace with your API URL

st.set_page_config(page_title="Chatbot HabiCredit", layout="wide")
st.title("🏡 Habicredit Chatbot")

query = st.text_input("Realiza las preguntas que hacen tus brokers:")

if st.button("Responder") and query:
    response = requests.get(API_URL, params={"query": query})
    

    if response.status_code == 200:
        st.write("🔍 Respuesta:", response.json().get("response", "⚠️ No 'response' key found in JSON."))
    else:
        st.error(f"❌ API Error: {response.status_code}")
