from langchain_huggingface import HuggingFaceEmbeddings
from preprocessing import clean_and_chunk
from langchain_community.vectorstores import FAISS
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))
from config import (FILE_PATHS,EMBEDDING_MODELS)


model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
hf = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODELS[0],
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
hf2 = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODELS[1],
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
file_path1 = str(FILE_PATHS[1])
file_path2 = str(FILE_PATHS[0])
file_path3 = str(FILE_PATHS[3])
file_path4 = str(FILE_PATHS[2])

c1,c2,c3,c4 = clean_and_chunk(file_path1,file_path2,file_path3,file_path4)
all_chunks = c1+c2+c3+c4
texts = [f"passage: {doc.page_content}" for doc in all_chunks]
metadatas = [doc.metadata for doc in all_chunks]

# vectorstore = FAISS.from_texts(texts, hf, metadatas=metadatas)
# vectorstore.save_local("faiss_index_bge")
# print("FAISS index saved at 'faiss_index_bge'")

vectorstore2 = FAISS.from_texts(texts, hf2, metadatas=metadatas)
vectorstore2.save_local("faiss_index_e5")
print("FAISS index saved at 'faiss_index_e5'")


