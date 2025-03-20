import streamlit as st
import requests

API_URL = "https://api1-zv36.onrender.com/chat"  # Replace with your API URL

st.set_page_config(page_title="Chatbot HabiCredit", layout="wide")
st.title("🏡 Habicredit Chatbot --")

## query = st.text_input("Realiza las preguntas que hacen tus brokers:")

with st.form(key='my_form'):
    query = st.text_input("Escribe algo y presiona Enter o el botón:")
    ## submit_button = st.form_submit_button(label='Enviar')

if st.form_submit_button(label='Enviar') and query:
    response = requests.get(API_URL, params={"query": query})
    

    if response.status_code == 200:
        st.write("🔍 Respuesta:", response.json().get("response", "⚠️ No 'response' key found in JSON."))
    else:
        st.error(f"❌ API Error: {response.status_code}")
