from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from agents.scheduler_agent import handle_meeting_request
from rag.chain import build_retrieval_chain
from agents.graph import agent
from langchain_core.messages import HumanMessage

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

@app.post("/schedule")
def schedule_meeting(request: QueryRequest):
    response = handle_meeting_request(request.question)
    return {"response": response}


@app.post("/chat")
def chat(req: QueryRequest):
    response = agent.invoke({
        "messages": [
             HumanMessage(content=req.question)
        ]
    })

    return {
        "response": response["messages"][-1].content
    }