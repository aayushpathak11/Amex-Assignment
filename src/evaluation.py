from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv()


os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


embedding_model = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

def get_embedding(text):
    return embedding_model.embed_query(text)

def evaluate_rag_output(question, answer, contexts):

    answer_embedding = embedding_model.embed_query(answer)
    context_text = " ".join(contexts)
    context_embedding = embedding_model.embed_query(context_text)
    question_embedding = embedding_model.embed_query(question)


    context_similarity = cosine_similarity([answer_embedding], [context_embedding])[0][0]

    answer_relevance = cosine_similarity([question_embedding], [answer_embedding])[0][0]


    prompt = (
        "Given the context and the answer, rate the faithfulness of the answer to the context "
        "on a scale of 0 (not faithful) to 1 (fully faithful).\n\n"
        f"Context:\n{' '.join(contexts)}\n\n"
        f"Answer:\n{answer}\n\n"
        "Respond with a single float between 0 and 1."
    )
    try:
        response = llm.invoke(prompt).content.strip()
        faithfulness = float(response)
    except (ValueError, AttributeError):
        faithfulness = 0.0  


    return {
        "context_similarity": context_similarity,
        "answer_relevance": answer_relevance,
        "faithfulness": faithfulness
    }
