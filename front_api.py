import streamlit as st
import requests

API_URL = "https://api1-zv36.onrender.com/chat"  # Replace with your API URL

st.set_page_config(page_title="Chatbot HabiCredit", layout="wide")
st.title("🏡 Habicredit Chatbot 3")

## CSS
st.markdown("""
    <style>
    .stButton>button:hover {
        background-color: #4CAF50; /* Green */
        color: white;
    }

    /* CSS for changing the border color of the text input box */
    .stTextInput>div>div>input {
        border: 2px solid #3498db; /* Blue border color */
    }

    /* CSS for changing the border color of the entire form */
    .stForm {
        border: 2px solid #3498db; /* Blue border color */
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Usa st.form para agrupar el input y botón
with st.form(key='chat_form'):
    query = st.text_input("Realiza las preguntas que hacen tus brokers:")
    submit_button = st.form_submit_button(label='Responder')

if submit_button and query:
    response = requests.get(API_URL, params={"query": query})

    if response.status_code == 200:
        st.write("🔍 Respuesta:", response.json().get("response", "⚠️ No 'response' key found in JSON."))
    else:
        st.error(f"❌ API Error: {response.status_code}")
