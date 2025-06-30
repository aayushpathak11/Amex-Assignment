from langchain_huggingface import HuggingFaceEmbeddings
from preprocessing import clean_and_chunk
from langchain_community.vectorstores import FAISS
# model_name = "sentence-transformers/all-mpnet-base-v2"
model_name = "BAAI/bge-base-en-v1.5"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
file_path1 = r"D:\Amex-Assignment\documents\Financial Policies (PDF).pdf"
file_path2 = r"D:\Amex-Assignment\documents\a_2.1_financial_policy_manual_lubbock_chamber_of_commerce_11.19.pdf"
file_path3 = r"D:\Amex-Assignment\documents\Sample-Nonprofit-Financial-Policies-and-Procedures-Manual-Resource.pdf"
file_path4 = r"D:\Amex-Assignment\documents\sample_fin_mgmt_policy.pdf"

c1,c2,c3,c4 = clean_and_chunk(file_path1,file_path2,file_path3,file_path4)
all_chunks = c1+c2+c3+c4
texts = [f"passage: {doc.page_content}" for doc in all_chunks]
metadatas = [doc.metadata for doc in all_chunks]

vectorstore = FAISS.from_texts(texts, hf, metadatas=metadatas)
vectorstore.save_local("faiss_index_bge")
print("FAISS index saved at 'faiss_index_bge'")
# v1 = hf.embed_documents([doc.page_content for doc in c1])
# v2 = hf.embed_documents([doc.page_content for doc in c2])
# v3 = hf.embed_documents([doc.page_content for doc in c3])
# v4 = hf.embed_documents([doc.page_content for doc in c4])
# vector = v1+v2+v3+v4

