from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from rag.chain import build_retrieval_chain

app = FastAPI()

load_dotenv()

retrieval_chain = build_retrieval_chain()


@app.on_event("startup")
def announce_startup() -> None:
    print("App is running at http://127.0.0.1:8000")
    print("Swagger is running at http://127.0.0.1:8000/docs")

class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QueryRequest):
    result = retrieval_chain.invoke({"input": request.question})

    return {
        "answer": result["answer"],
        "sources": [
            doc.metadata for doc in result.get("context", [])
        ]
    }