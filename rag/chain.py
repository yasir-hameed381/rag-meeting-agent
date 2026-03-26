from langchain_mistralai import ChatMistralAI
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from rag.prompts import CUSTOM_PROMPT
from rag.retriever import load_vectorstore

def build_retrieval_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatMistralAI(
        model_name="mistral-small",  # note: 'model' not 'model_name'
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(CUSTOM_PROMPT)
    print("Prompt template loaded successfully.", prompt)
    print("Custom prompt:", CUSTOM_PROMPT)

    # Combines the retrieved docs + prompt + LLM
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    print("Combine docs chain created successfully.",combine_docs_chain)

    # Wraps retriever + combine_docs_chain together
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
    print("Retrieval chain created successfully.", retrieval_chain)

    return retrieval_chain