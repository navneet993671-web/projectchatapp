import streamlit as st
import ollama

st.set_page_config(page_title="Local Chatbot", layout="centered")

st.title("🤖 Local Chatbot (Ollama)")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2:1b",
        messages=st.session_state.messages
    )

    bot_reply = response["message"]["content"]

    # Show bot reply
    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    