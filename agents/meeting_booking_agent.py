from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware, SummarizationMiddleware 
from langchain_mistralai import ChatMistralAI

from tools.meeting_booking_tool import schedule_meeting_tool

load_dotenv()

llm = ChatMistralAI(
    model_name="mistral-small",
    temperature=0,
)

tools = [schedule_meeting_tool]

# Keep RAG optional so the meeting booking agent can boot
# even when FAISS/vector index dependencies are not installed.
try:
    from tools.rag_tool import rag_tool

    tools.append(rag_tool)
except Exception as exc:
    print(f"RAG tool disabled: {exc}")

agent = create_agent(
    llm,
    tools,
    middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
        PIIMiddleware(
            "api_key",
            detector=r"sk-[a-zA-Z0-9]{32}",
            strategy="block",
        ),
        SummarizationMiddleware(
            llm,
            trigger=("messages", 5),
            keep=("messages", 20),
        )
    ],
)
