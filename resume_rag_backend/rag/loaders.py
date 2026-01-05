from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .vectorDb import create_vector_db_or_load

# Path to the PDF (two folders up from this script)
file_path = Path(__file__).parent.parent / "masterResume.pdf"



def splitter(document):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
   
    texts = text_splitter.split_documents(document)
    
    return texts    

def file_loader():
    """Load the data from the PDF file"""
    if file_path.exists():
        loader = PyPDFLoader(str(file_path))  # convert Path to string
        data = loader.load()
        splitter_data= splitter(data)
        vector_db = create_vector_db_or_load(splitter_data)
        print(vector_db)    
        return vector_db
    else:
        raise Exception(f"File not found: {file_path}")
