from core.query import search_chroma
from ollama import chat
from ollama import ChatResponse
from langchain_core.prompts import PromptTemplate
_CHAT_MODEL = 'mistral'

def ask_handbook(question):
    results = search_chroma(question)
    context_text = results['documents'][0]
    response = chat(
        model = _CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content" : f"You are a helpful university assistant. You can only answer the information provided. {context_text}"
            },
            {
                "role" : "user",
                "content" : question 
            }

        ]
    )
    return response["message"]["content"]



if __name__ == "__main__":
    while True:
        q = input("\nAsk handbook (type 'exit'): ")
        if q.lower() == "exit":
            break

        answer = ask_handbook(q)
        print("\n📘 Answer:\n", answer)