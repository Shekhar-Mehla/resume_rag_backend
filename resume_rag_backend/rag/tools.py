from langchain.tools import tool
from langchain.tools import tool
from .loaders import db_loader

@tool(description="Fetches relevant information from Shekhar's resume: skills, projects, experience, or education only.")
def get_context_from_resume(query: str) -> str:
    """
    Retrieve relevant resume chunks from vector database based on user query.
    Returns a single string concatenating relevant chunks.
    """
    # Get retriever from vector DB
    retriever = db_loader().as_retriever(search_type="similarity", search_kwargs={"k": 2})

    # Use public method for retrieval
    relevant_docs = retriever.get_relevant_documents(query)

    if not relevant_docs:
        # Fallback if nothing is found
        return "I am Shekhar's resume assistant. How can I help you?"

    # Optionally filter by section based on query keywords
    query_lower = query.lower()
    filtered_docs = []
    for doc in relevant_docs:
        section = doc.metadata.get("section", "").lower()
        if ("skill" in query_lower and "skills" in section) or \
           ("project" in query_lower and "projects" in section) or \
           ("education" in query_lower and "education" in section) or \
           ("experience" in query_lower and "experience" in section):
            filtered_docs.append(doc)

    # If filtering yields nothing, just use top retrieved docs
    final_docs = filtered_docs or relevant_docs

    # Serialize the content for LLM input
    serialized_doc = "\n".join([doc.page_content for doc in final_docs])

    return serialized_doc
