from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from dotenv import load_dotenv
from tools.calendar_tool import schedule_meeting_tool
from tools.rag_tool import rag_tool

load_dotenv()

llm = ChatMistralAI(
    model_name="mistral-small",
    temperature=0
)

tools = [
    schedule_meeting_tool,
    rag_tool
]

agent = create_agent(llm, tools)