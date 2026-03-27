from typing import Any

from langchain_mistralai import ChatMistralAI

from rag.prompts import CUSTOM_PROMPT
from rag.retriever import load_vectorstore


class SimpleRetrievalChain:
    """Small replacement for legacy chain imports removed in LangChain 1.x."""

    def __init__(self) -> None:
        vectorstore = load_vectorstore()
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        self.llm = ChatMistralAI(model_name="mistral-small", temperature=0)

    def invoke(self, inputs: dict[str, Any]) -> dict[str, Any]:
        question = inputs.get("input", "").strip()
        docs = self.retriever.invoke(question)

        context = "\n\n".join(doc.page_content for doc in docs)
        prompt = CUSTOM_PROMPT.format(context=context, input=question)

        answer = self.llm.invoke(prompt).content
        return {"answer": answer, "context": docs}


def build_retrieval_chain() -> SimpleRetrievalChain:
    return SimpleRetrievalChain()