from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
model_name = "BAAI/bge-base-en-v1.5"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}

hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)


vectorstore = FAISS.load_local("faiss_index_bge", hf,allow_dangerous_deserialization=True)


retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})


def retrieve_context(query):
    query = query
    context = []
    results_with_scores = vectorstore.similarity_search_with_score(f"passage: {query}", k=8)
    # results = retriever.get_relevant_documents(f"passage: {query}")
    # for i, doc in enumerate(results, 1):
    #     print(f"\n--- Result {i} ---\n{doc.page_content}")
    for i, (doc, score) in enumerate(results_with_scores, 1):
        print(f"\n--- Result {i} ---")
        print(f"Score: {score:.4f}")
        print(f"Content:\n{doc.page_content}")
        context.append(doc.page_content)
    return context
