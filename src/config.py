from pathlib import Path
import os
BASE_DIR = Path(__file__).parent.resolve()
DOCUMENTS_DIR = (BASE_DIR.parent / "documents").resolve() 

FILE_PATHS = [
    DOCUMENTS_DIR/"a_2.1_financial_policy_manual_lubbock_chamber_of_commerce_11.19.pdf",
    DOCUMENTS_DIR/"Financial Policies (PDF).pdf",
    DOCUMENTS_DIR/"sample_fin_mgmt_policy.pdf",
    DOCUMENTS_DIR/"Sample-Nonprofit-Financial-Policies-and-Procedures-Manual-Resource.pdf"
]

EMBEDDING_MODELS = [
    "BAAI/bge-base-en-v1.5",
    "intfloat/e5-large-v2"
]

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

VECTORSTORE_OPTIONS = [
    "e5",
    "bge"
]

TOP_K = [5,10,15,20]
TOP_N = [3,5,8,10]