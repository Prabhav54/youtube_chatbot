import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HF_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    
    # Hugging Face Models
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_REPO_ID = "HuggingFaceH4/zephyr-7b-beta"
    
    # Text Splitting Parameters
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200