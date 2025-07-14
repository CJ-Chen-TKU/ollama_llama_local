# 🤖 Local LLM Chatbot with Ollama + Streamlit

This project is a local chatbot app built with **Streamlit** and powered by **Ollama**, running large language models (LLMs) like **LLaMA 2** and **LLaMA 3** on your own machine.

The app supports:
- Real-time chat with streaming responses
- Fast local inference via [Ollama](https://ollama.com/)
- Easy switching between models
- Chat history management
- Response time tracking

---

## 🚀 Features

✅ Run LLMs locally (no cloud APIs or internet needed)  
✅ Streamlit chat interface with `chat_input`  
✅ Real-time streaming via `llama-index-llms-ollama`  
✅ Logs response time  
✅ Works with models like `llama3`, `llama2`, and more via Ollama

---

## 🛠 Installation

### 1. Install Ollama

> [Download Ollama](https://ollama.com/download) and follow the instructions to install on your system.

Make sure it's running:

```bash
ollama serve

### 2. Install Python dependencies

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required packages:
pip install -r requirements.txt

requirements.txt:
streamlit
ollama
llama-index-llms-ollama

Start the app:
streamlit run ollama_llama_local.py

Then open the URL (usually http://localhost:8501) in your browser.

