from langchain_community.vectorstores import FAISS
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))
from config import (FILE_PATHS,EMBEDDING_MODELS)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain.retrievers import ContextualCompressionRetriever


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

vectorstore = FAISS.load_local("faiss_index_bge", hf,allow_dangerous_deserialization=True)

vectorstore2 = FAISS.load_local("faiss_index_e5", hf2,allow_dangerous_deserialization=True)

cross_encoder = HuggingFaceCrossEncoder(
    model_name="BAAI/bge-reranker-base",
    model_kwargs={"device": "cpu"}
)


def retrieve_context(query,choice,top_k,top_n):
    reranker = CrossEncoderReranker(model=cross_encoder, top_n=top_n)
    context = []
    if choice=='e5':
        chosen_vectorstore = vectorstore2
    else :
        chosen_vectorstore = vectorstore

    compression_retriever = ContextualCompressionRetriever(
        base_retriever=chosen_vectorstore.as_retriever(search_kwargs={"k": top_k}),
        base_compressor=reranker
    )

    docs = compression_retriever.invoke(query)

    for doc in docs:
        context.append(doc.page_content)

    return context

