import streamlit as st
from sidebar import display_sidebar
from chat_interface import display_chat_interface

st.title("My Document Chatbot")

# initialize Session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None


# display the sidebar
display_sidebar()

# display the chat interface
display_chat_interface()
