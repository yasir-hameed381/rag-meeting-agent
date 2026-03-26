from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from tools.calendar_tool import schedule_meeting_tool
from tools.rag_tool import rag_tool
from langchain.agents.middleware import SummarizationMiddleware


load_dotenv()

llm = ChatMistralAI(
    model_name="mistral-small",
    temperature=0
)

checkpointer = InMemorySaver()

tools = [
    schedule_meeting_tool,
    rag_tool
]

agent = create_agent(
    llm, 
    tools , 
    checkpointer=checkpointer, 
    middleware=[
        SummarizationMiddleware(
            llm,
            trigger=("tokens", 4000),
            keep=("messages", 20))
        ])