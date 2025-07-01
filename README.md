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

## Questions
### What Strategy did i use and why?
- I tried many possible combinations at each step , for chunking, for embedding model, for chunk size, chunk overlap, for retrieval (with and without reranker) and decided to choose among them which worked most efficiently. In detailed approach of each step is written in approach.txt

### Challenges Faced
- While selecting open-source LLM , I faced several challenges, small (less parameters) models were not performing well, and larger models were requiring a lot of gpu compute, thus introducing a lot of latency in the pipeline, Hence I chose to go with gemini 2.0 flash free api.
- I had no idea of how to evaluate rag systems quantitatively, hence did a lot of research and studied frameworks like RAGAS and Deepeval. But while implementing both of them i was facing certain openai key error, perhaps both of them required openai key to work and i did not have that. Then i did more research , took help of chatgpt to come up with own metrics to calculate cosine similarity between chunks, questions and answer generated to check their relevancy and groundedness.
- I though of deploying the app for better usage and easy assessment, I faced several difficulties on the deployment part also.

### How would system behave for conflicting information
- The ingestion pipeline has not been distinguished as per document files, all the chunks from each file are stored in a single vectorstore. So when user asks a query which may be present in multiple files, similarity search and after that crossencoder based reranker would pick up the specified number of most relevant chunks to that query.
- So it is completely possible that answer would be formed from information of multiple pdfs if the reranked chunks are in such a way.

## Sample Screenshots of working demo
#### Sample 1 - Demo - ![random_question-1](https://github.com/user-attachments/assets/b0699417-a4ce-4ea9-81ba-a694db25cc8e) 
### Actual Answer in Documents ![random_question-1_groundtruth](https://github.com/user-attachments/assets/c529edee-ffc6-4c70-957e-532f162bf009)

### Sample 2 - Demo - ![random_question-3](https://github.com/user-attachments/assets/ad60b762-97fa-4fb6-a94b-e43c29ef057f)
### Actual Answer in Documents 
![random_queston-3_groundtruth](https://github.com/user-attachments/assets/1430a8ad-cd50-42e4-94d0-6ff31a7cd71b)



