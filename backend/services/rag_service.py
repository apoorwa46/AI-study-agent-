from tools.pdf_loader import load_pdf
from tools.text_splitter import split_documents
from tools.embeddings import get_embedding_model
from tools.vector_store import create_vector_store, load_vector_store

from backend.services.ollama_service import get_llm

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# 🔹 STEP 1: Process PDF → store embeddings
def process_pdf(file_path: str):
    # Load PDF 
    documents = load_pdf(file_path)
    # Split into chunks
    chunks = split_documents(documents)
    # Get embedding model
    embedding_model = get_embedding_model()
    # Create vector store
    create_vector_store(chunks, embedding_model)


# 🔹 STEP 2: Create QA Chain
def get_qa_chain():
    # get embedding model
    embedding_model = get_embedding_model()
    # load vector store
    vector_store = load_vector_store(embedding_model)

    retriever = db.as_retriever(search_kwargs={"k": 4})

    # get LLM
    llm = get_llm()

    prompt_template = """
You are a helpful AI tutor.

Use ONLY the provided context to answer the question.

If the answer is not in the context, say:
"I couldn't find this in the document."

Context:
{context}

Question:
{question}

Answer:
"""
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriever,
        chain_type = "stuff",
        chain_type_kwargs = {"prompt": prompt}
    )

    return qa_chain


# 🔹 STEP 3: Ask Question
def ask_question(query: str):
    qa_chain = get_qa_chain()
    response = qa_chain.run(query)
    return response

