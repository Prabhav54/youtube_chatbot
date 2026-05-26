from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from src.config import Config

def create_vector_store(chunks):
    """Generates embeddings and stores them in FAISS."""
    embeddings = HuggingFaceEmbeddings(model_name=Config.EMBEDDING_MODEL)
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

def get_retriever(vector_store):
    """Returns a retriever configured for similarity search."""
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})