from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv()

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize HF Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# Gemini LLM for scoring
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

def get_embedding(text):
    return embedding_model.embed_query(text)

def compute_context_similarity(question,answer, contexts):
    # Compute context similarity (Context Recall proxy)
    context_text = " ".join(contexts)
    answer_embedding = get_embedding(answer)
    context_embedding = get_embedding(context_text)
    context_similarity = cosine_similarity(answer_embedding, context_embedding)[0][0]

    # Compute answer relevance: how similar the answer is to the question
    question_embedding = get_embedding(question)
    answer_relevance_score = cosine_similarity(answer_embedding, question_embedding)[0][0]

    return {
        "context_similarity": context_similarity,
        "answer_relevance": answer_relevance_score
    }


def compute_llm_faithfulness(question, answer, contexts):
    prompt = (
        "Given the question:\n"
        f"{question}\n\n"
        "And the answer:\n"
        f"{answer}\n\n"
        "And the context:\n"
        f"{' '.join(contexts)}\n\n"
        "On a scale of 0 (inaccurate) to 1 (fully faithful), how faithful is the answer to the context? "
        "Only return a float between 0 and 1."
    )
    try:
        response = llm.invoke(prompt).content.strip()
        return float(response)
    except:
        return 0.0  # fallback if Gemini fails

def evaluate_rag_output(question, answer, contexts):
    """
    Calculates all RAG evaluation scores and returns them in a single, flat dictionary.
    """
    # 1. Generate Embeddings
    answer_embedding = embedding_model.embed_query(answer)
    context_text = " ".join(contexts)
    context_embedding = embedding_model.embed_query(context_text)
    question_embedding = embedding_model.embed_query(question)

    # 2. Calculate Similarity Scores
    # The [0][0] is crucial to extract the float value from the 2D numpy array
    context_similarity = cosine_similarity([answer_embedding], [context_embedding])[0][0]

    answer_relevance = cosine_similarity([question_embedding], [answer_embedding])[0][0]

    # 3. Calculate LLM-based Faithfulness
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
        faithfulness = 0.0  # Fallback if LLM fails or returns non-float

    # 4. Return all scores in a single, flat dictionary
    return {
        "context_similarity": context_similarity,
        "answer_relevance": answer_relevance,
        "faithfulness": faithfulness
    }
