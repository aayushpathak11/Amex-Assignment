from langchain_community.vectorstores import FAISS
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))
from config import (FILE_PATHS,EMBEDDING_MODELS,VECTORSTORE_BGE_PATH,VECTORSTORE_E5_PATH)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain.retrievers import ContextualCompressionRetriever


model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}

# bge-base embedding model object
hf = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODELS[0],
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# e5-large-v2 embedding model object
hf2 = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODELS[1],
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# vectorstore for bge model
vectorstore = FAISS.load_local(VECTORSTORE_BGE_PATH, hf,allow_dangerous_deserialization=True)

# vectorstore for e5 model
vectorstore2 = FAISS.load_local(VECTORSTORE_E5_PATH, hf2,allow_dangerous_deserialization=True)

# reranking configuration - used bge-reranker-base from huggingface
cross_encoder = HuggingFaceCrossEncoder(
    model_name="BAAI/bge-reranker-base",
    model_kwargs={"device": "cpu"}
)


def retrieve_context(query,choice,top_k,top_n):
    # Function responsible to retrieve context using the right vectorstore and right configurations chosen

    # dynamically setting the no of reranked chunks
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

