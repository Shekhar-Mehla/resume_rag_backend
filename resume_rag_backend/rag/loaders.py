from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

# Path to the PDF (two folders up from this script)
file_path = Path(__file__).parent.parent / "masterResume.pdf"

def file_loader():
    """Load the data from the PDF file"""
    if file_path.exists():
        loader = PyPDFLoader(str(file_path))  # convert Path to string
        data = loader.load()
        return data
    else:
        raise Exception(f"File not found: {file_path}")
