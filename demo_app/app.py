import streamlit as st
import os, sys
from pathlib import Path
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))
from retriever import retrieve_context
from generation import answer_with_gemini
from evaluation import evaluate_rag_output
from config import VECTORSTORE_OPTIONS,TOP_K,TOP_N
from utils import log_answer

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("FINANCE RAG Chatbot")

# option to select vectorstore
vectorstore_option = st.sidebar.selectbox(
    "Select Vectorstore for Retrieval : ",
    options=VECTORSTORE_OPTIONS,
)

#option to select number of chunks
top_k_option = st.sidebar.selectbox(
    "Select Number of Chunks : ",
    options=TOP_K,
)

#option to select number of reranked chunks
top_n_option = st.sidebar.selectbox(
    "Select Number of Chunks after reranking: ",
    options=TOP_N,
)
st.sidebar.write("NOTE: Number of Chunks should be more than rerank number")
# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display conversation history
for entry in st.session_state.history:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])


if user_input := st.chat_input("Ask a question about your documents…"): 
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    chunks = retrieve_context(user_input,choice=vectorstore_option,top_k=top_k_option,top_n=top_n_option) # retrieving chunks using appropriate configurations
    answer = answer_with_gemini(user_input,chunks) # generating answer
    log_answer(user_input,chunks,answer,vectorstore_option,top_k_option,top_n_option) # logging results
    scores = evaluate_rag_output(user_input, answer, chunks) #evaluating scores

    st.session_state.history.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        col1, col2 = st.columns([3, 1]) 
        with col1:
            st.markdown(answer)
            with st.expander("Evaluation Scores"):
                st.write(f"**Context Similarity**: {scores['context_similarity']:.2f}")
                st.write(f"**Answer Relevance**: {scores['answer_relevance']:.2f}")
                st.write(f"**Faithfulness (LLM)**: {scores['faithfulness']:.2f}")
        with col2:
            st.subheader("Retrieved Contexts")
            for i, chunk in enumerate(chunks):
                with st.expander(f"Chunk {i+1}"):
                    st.write(chunk)

if st.sidebar.button("⚙️ Clear Chat"):
    st.session_state.history.clear()
