from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_DB_DIR = Path("./chroma_langchain_db").resolve()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_db_or_load(documents=None):
    print(documents)

    if VECTOR_DB_DIR.exists():
        print("📦 Loading existing vector DB")

        return Chroma(
            persist_directory=str(VECTOR_DB_DIR),   
            embedding_function=embeddings           
            
        )

    print("🧠 Creating new vector DB")

    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=str(VECTOR_DB_DIR)
    )
