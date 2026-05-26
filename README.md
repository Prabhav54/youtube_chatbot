# 🎥 YouTube RAG Chatbot: AI-Powered Video Assistant

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-lightgrey)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-🤗-yellow)

An interactive Retrieval-Augmented Generation (RAG) application that allows users to chat directly with YouTube videos. By extracting video transcripts and processing them through a locally managed vector database, this bot provides highly accurate, context-aware answers to user queries using open-source Large Language Models.

## 🚀 Features
* **Instant Transcript Extraction:** Bypasses manual transcription by programmatically fetching YouTube captions.
* **Semantic Search:** Uses Hugging Face `all-MiniLM-L6-v2` embeddings and FAISS to chunk, embed, and retrieve the most relevant video context.
* **Conversational AI:** Powered by the `Zephyr-7B-Beta` LLM for fluid, intelligent, and accurate responses grounded *only* in the video's content.
* **Modular Architecture:** Clean, production-ready codebase separating data ingestion, augmentation, retrieval, and generation.
* **Interactive Web UI:** Built with Streamlit for a seamless, chat-like user experience.

## 🏗️ Project Structure
```text
youtube_chatbot/
├── .env                    # API keys and environment variables
├── requirements.txt        # Project dependencies
├── app.py                  # Streamlit frontend
└── src/                    # Modular backend
    ├── __init__.py
    ├── config.py           # Centralized configuration and model tracking
    ├── ingest.py           # YouTube API transcript fetching and text splitting
    ├── retrieval.py        # FAISS vector store and embedding logic
    ├── augmentation.py     # Prompt engineering and LCEL formatting
    └── generation.py       # Hugging Face API LLM initialization


⚙️ Installation & Setup
1. Clone the repository

Bash
git clone [https://github.com/yourusername/youtube-rag-chatbot.git](https://github.com/yourusername/youtube-rag-chatbot.git)
cd youtube-rag-chatbot
2. Create a virtual environment (Conda recommended)

Bash
conda create -n yt_chatbot python=3.10 -y
conda activate yt_chatbot
3. Install dependencies

Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your Hugging Face API token:

Code snippet
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token_here
💻 Usage
Fire up the Streamlit server to launch the application:

Bash
streamlit run app.py
Paste any YouTube URL into the sidebar.

Click Process Transcript to build the vector database in real-time.

Start asking questions about the video in the chat interface!

🧠 Future Scope
Implement Whisper API for videos without pre-generated closed captions.

Add multi-video support to query across an entire YouTube playlist or channel.

Integrate memory buffers to retain conversation history across multiple queries.

Author: Prabhav Khare


This RAG project pairs brilliantly with your other predictive analytics work. Are you planning to link this repository directly on your resume, or will you be deploying it live (e.g., on Streamlit Community Cloud) so recruiters can test it themselves?
