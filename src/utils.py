import json
import os
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))
from config import (EXAMPLE_LOG_FILE)

def log_answer(question, chunks, answer,vectorstore_option,top_k_option,top_n_option):

    entry = {
        "question": question,
        "chunks": chunks,
        "answer": answer,
        "configurations": f"Vector Store: {vectorstore_option}, TOP_K: {top_k_option}, TOP_N: {top_n_option}"
    }

    with open(EXAMPLE_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry)+'\n')
