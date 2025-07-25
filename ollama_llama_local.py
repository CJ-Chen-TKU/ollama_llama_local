 # py code beginning

import streamlit as st
import logging
import time

from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

# ------------------ Setup ------------------
logging.basicConfig(level=logging.INFO)

if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ Stream Chat ------------------
def stream_chat(model, messages):
    try:
        llm = Ollama(model=model, request_timeout=120)
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
        for r in resp:
            response += r.delta
            response_placeholder.write(response)
        logging.info(f"Model: {model}, Messages: {messages}, Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error during streaming: {str(e)}")
        raise e

# ------------------ Main UI ------------------
def main():
    st.set_page_config(page_title="Local LLM Chat", layout="centered")
    st.title("🤖 Local LLM at Home")

    model = st.sidebar.selectbox("請選擇模型 (Ollama)", ["llama3:latest", "llama2:latest"])
    logging.info(f"Model selected: {model}")

    if prompt := st.chat_input("Your question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        logging.info(f"User input: {prompt}")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            start_time = time.time()
            logging.info("Generating response")

            with st.spinner("Writing ..."):
                try:
                    messages = [
                        ChatMessage(role=msg["role"], content=msg["content"])
                        for msg in st.session_state.messages
                    ]
                    response_message = stream_chat(model, messages)
                    duration = time.time() - start_time
                    response_with_duration = f"{response_message}

🕒 Duration: {duration:.2f} sec"

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response_with_duration
                    })
                    st.write(response_with_duration)
                except Exception as e:
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": str(e)
                    })
                    st.error("An error occurred while generating the response.")
                    logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

