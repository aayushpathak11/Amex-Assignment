# Document Insights Prototype

## Architecture of the Solution
![architecture](https://github.com/user-attachments/assets/3fbb59e2-7e25-4417-a061-979ae86c05c2)

## Some Points
- I have deployed the app for ease of use - https://amex-assignment-financerag.streamlit.app/
- Detailed steps and logical approach is explained in approach.txt
- Have used open source embedding models bge-base-en and e5-large-v2 for embeddings
- Have used FAISS as a vector store
- Used huggingface bge-reranker for reranking the retrieved chunks
- Used Gemini 2.0 flash as LLM for answer generation
- Have created a streamlit app for the RAG pipeline
- The app has an option to select vectorstore at runtime and displays answer of the question as well as chunks retrieved along with the evaluation scores

## Sample Screenshots of working demo
#### Sample 1 - Demo - ![random_question-1](https://github.com/user-attachments/assets/b0699417-a4ce-4ea9-81ba-a694db25cc8e) 
### Actual Answer in Documents ![random_question-1_groundtruth](https://github.com/user-attachments/assets/c529edee-ffc6-4c70-957e-532f162bf009)

### Sample 2 - Demo - ![random_question-3](https://github.com/user-attachments/assets/ad60b762-97fa-4fb6-a94b-e43c29ef057f)
### Actual Answer in Documents 
![random_queston-3_groundtruth](https://github.com/user-attachments/assets/1430a8ad-cd50-42e4-94d0-6ff31a7cd71b)



