from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from rag.ingest import get_chunks
import os

DB_PATH = "vectorstore/faiss_index"

def create_vectorstore():
    chunks = get_chunks()
    if not chunks:
        raise ValueError(
            "No content found in data/raw or configured web sources. "
            "Add at least one .pdf/.txt file or verify website loading."
            "before building the vectorstore."
        )
    embeddings = MistralAIEmbeddings()

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(DB_PATH)

    print(f"Vectorstore created and saved at {DB_PATH}")
    return vectorstore


def load_vectorstore():
    embeddings = MistralAIEmbeddings()

    if not os.path.exists(DB_PATH):
        return create_vectorstore()

    vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    print(f"Vectorstore loaded from {DB_PATH}")
    return vectorstore