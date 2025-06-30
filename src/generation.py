import os
from langchain_google_genai import ChatGoogleGenerativeAI
from retriever import retrieve_context  


os.environ["GOOGLE_API_KEY"] = "AIzaSyCTqx8YU1BKUwv_H218qmKm7MROTDR7yLo"


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.0)


def build_prompt(context: str, question: str) -> str:
    return f"""You are a helpful AI assistant. Use the following context to answer the question.
If the answer is not found in the context, say "I couldn't find the answer in the documents."

Context:
{context}

Question:
{question}

Answer:
"""


def answer_with_gemini(query: str) -> str:
    docs = retrieve_context(query)
    if not docs:
        return "No relevant context found."

    context = "\n\n".join(docs)
    prompt = build_prompt(context, query)

    response = llm.invoke(prompt)
    return response.content.strip()


def answer(question):
    # question = "What is the procedure for financial approval outlined in the policies?"
    answer = answer_with_gemini(question)
    return answer
