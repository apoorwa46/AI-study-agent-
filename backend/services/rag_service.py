from tools.pdf_loader import load_pdf
from tools.text_splitter import split_documents
from tools.embeddings import get_embedding_model
from tools.vector_store import create_vector_store, load_vector_store

from backend.services.ollama_service import get_llm

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 🔹 Process PDF
def process_pdf(file_path: str):
    documents = load_pdf(file_path)
    chunks = split_documents(documents)

    embedding_model = get_embedding_model()
    create_vector_store(chunks, embedding_model)


# 🔹 Ask Question (NEW STYLE)
def ask_question(query: str):
    embedding_model = get_embedding_model()
    db = load_vector_store(embedding_model)

    retriever = db.as_retriever(search_kwargs={"k": 4})

    llm = get_llm()

    # 🔥 Prompt
    prompt = PromptTemplate.from_template("""
You are a helpful AI tutor.

Use ONLY the context below to answer the question.
If answer not found, say: "Not found in document."

Context:
{context}

Question:
{question}

Answer:
""")

    # 🔹 Retrieve docs
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    # 🔹 Format prompt
    final_prompt = prompt.format(context=context, question=query)

    # 🔹 Call LLM
    response = llm.invoke(final_prompt)

    return response