import streamlit as st
import re
from src.ingest import get_transcript_and_split
from src.retrieval import create_vector_store, get_retriever
from src.generation import build_rag_chain

st.set_page_config(page_title="YouTube RAG Chatbot", page_icon="🎥")

def extract_video_id(url):
    """Extracts the YouTube video ID from a standard URL."""
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else url # Returns URL if it's already an ID

st.title("🎥 YouTube AI Chatbot")
st.markdown("Ask questions about any YouTube video using Hugging Face & FAISS.")

# Sidebar for processing the video
with st.sidebar:
    st.header("1. Process Video")
    video_input = st.text_input("Enter YouTube URL sor Video ID:")
    process_btn = st.button("Process Transcript")

# Initialize session state to store the RAG chain
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# Video Processing Logic
if process_btn and video_input:
    with st.spinner("Fetching transcript & building vector store..."):
        try:
            video_id = extract_video_id(video_input)
            
            # Use modular functions
            chunks = get_transcript_and_split(video_id)
            vector_store = create_vector_store(chunks)
            retriever = get_retriever(vector_store)
            
            st.session_state.rag_chain = build_rag_chain(retriever)
            st.success("Video processed successfully! You can now ask questions.")
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Chat Interface
st.header("2. Chat with the Video")

# Display chat messages from history on app rerun
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is this video about?"):
    if st.session_state.rag_chain is None:
        st.warning("Please process a video first!")
    else:
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.rag_chain.invoke(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error generating response: {e}")