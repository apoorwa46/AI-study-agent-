from langchain_community.vectorstores import FAISS
import os

VECTOR_DB_PATH = "data/vector_db"

def create_vector_store(documents, embedding_model):
    db = FAISS.from_documents(documents,embedding_model)
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    db.save_model(VECTOR_DB_PATH)
    return db

def load_vector_store(embedding_model):
    return FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )