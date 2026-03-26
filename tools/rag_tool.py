from langchain.tools import tool
from rag.chain import build_retrieval_chain
from dotenv import load_dotenv

load_dotenv()

retrieval_chain = build_retrieval_chain()

@tool
def rag_tool(question: str) -> str:
    """
    Answer questions about Technovez company, services, and information.
    """
    result = retrieval_chain.invoke({"input": question})
    return result["answer"]