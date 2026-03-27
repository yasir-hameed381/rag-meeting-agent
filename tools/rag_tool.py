from langchain.tools import tool
from dotenv import load_dotenv
from rag.chain import build_retrieval_chain

load_dotenv()

@tool
def rag_tool(question: str) -> str:
    """
    Answer questions about Technovez company, services, and information.
    """
    retrieval_chain = build_retrieval_chain()
    result = retrieval_chain.invoke({"input": question})
    return result["answer"]