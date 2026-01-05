from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path
path = Path(__file__).parent.parent/chroma_langchain_db



from langchain_chroma import Chroma
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")


def create_vector_db_or_load(documents):
    print(path)
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    
)

    vector_store = Chroma.from_documents(
    documents,
    embeddings,
    persist_directory="./chroma_langchain_db")
    return vector_store
  
  

