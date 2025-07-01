import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv() 

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.0)

def build_prompt(context: str, question: str) -> str:
    return f"""You are a helpful AI assistant for answering questions on Financial policy documents. Use the following context to answer the question.
If the answer is not found in the context, say "I couldn't find the answer in the documents."

Context:
{context}

Question:
{question}

Answer:
"""


def answer_with_gemini(query,chunks):
    # This function is responsible to generate answer using retrieved chunks with gemini 2.0 flash llm

    context = "\n\n".join(chunks)
    prompt = build_prompt(context, query)
    response = llm.invoke(prompt)
    return response.content.strip()

