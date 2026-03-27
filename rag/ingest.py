from langchain_community.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

DATA_PATH = "data/raw/"
WEB_SOURCES = ["https://www.technovez.com/"]

def load_documents():
    docs = []

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        else:
            continue

        docs.extend(loader.load())

    # Also ingest website content for company context.
    for url in WEB_SOURCES:
        try:
            web_loader = WebBaseLoader(url)
            docs.extend(web_loader.load())
        except Exception as exc:
            print(f"Skipping web source {url}: {exc}")

    return docs


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


def get_chunks():
    docs = load_documents()
    chunks = split_documents(docs)
    return chunks