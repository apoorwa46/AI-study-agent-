from langchain_community.llms import Ollama

def get_llm():
    return Ollama(
        model="gemma3:1b",
        temperature=0.7
    )

