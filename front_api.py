import streamlit as st
import requests

API_URL = "https://api1-zv36.onrender.com/chat"  # Replace with your API URL

st.set_page_config(page_title="Chatbot HabiCredit", layout="wide")
st.title("🏡 Habicredit Chatbot 3")

## CSS
st.markdown("""
    <style>
    .stButton>button:hover {
        background-color: #3498db; /* Green */
        color: white;
    }

     /* CSS for changing the border color and shadow of the text input box when focused */
    .stTextInput>div>div>input:focus {
        border: 2px solid #3498db; /* Red border color when focused */
        box-shadow: 2px 2px 5px rgba(255, 87, 51, 0.6); /* Red shadow when focused */
    }

    /* CSS for changing the border color of the text input box when focused */
    .stTextInput>div>div>input:focus {
        border: 2px solid #3498db; /* Red border color when focused */

    /* CSS for changing the border color and shadow of the entire form */
    .stForm {
        border: 2px solid #3498db; /* Blue border color */
        padding: 10px;
        border-radius: 5px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* Default shadow */
    }
    }

    /* CSS for changing the border color of the text input box */
    .stTextInput>div>div>input {
        border: 2px solid #3498db; /* Blue border color */
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
