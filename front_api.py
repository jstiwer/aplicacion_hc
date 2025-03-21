import streamlit as st
import requests

API_URL = "https://api1-zv36.onrender.com/chat"  # Replace with your API URL

# Ajusta el diseño con columnas
col1, col2 = st.columns([1, 1])

# Inserta la imagen en la primera columna y el título en la segunda
with col1:
    st.image("image__6_-removebg-preview.png", width=300)  # Reemplaza con la URL de tu imagen

with col2:
    st.title("Habicredit Chatbot 1")
    
## CSS
st.markdown("""
    <style>
    .stButton>button:hover {
        background-color: #c214de; /* Green */
        color: #c214de;
    }

    .stButton>button:focus {
        border: 2px solid #c214de; /* Red border color when focused */
        color: #c214de; /* Red text color when focused */
    }

    /* CSS for changing the border color and shadow of the text input box */
    .stTextInput>div>div>input {
        border: 2px solid #3498db; /* Blue border color */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Default shadow */
    }
    
    /* CSS for changing the border color and shadow of the text input box when focused */
    .stTextInput>div>div>input:focus {
        border: 2px solid #FF5733; /* Red border color when focused */
        box-shadow: 2px 2px 5px rgba(255, 87, 51, 0.6); /* Red shadow when focused */
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
