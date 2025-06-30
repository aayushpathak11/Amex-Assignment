import gradio as gr
import sys, os


sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))

from retriever import retrieve_context
from generation import answer_with_gemini

def chat_fn(message, history):

    history = history or []
    history.append({"role": "user", "content": message})
    

    chunks = retrieve_context(message)
    answer = answer_with_gemini(message)
    history.append({"role": "assistant", "content": answer})
    
    return history

with gr.Blocks() as demo:
    demo.title = "🧠 RAG Chatbot"
    chatbot = gr.Chatbot(type="messages")  
    msg = gr.Textbox(placeholder="Ask a question…")
    submit = gr.Button("Send")
    clear = gr.ClearButton([msg, chatbot])
    
    submit.click(chat_fn, [msg, chatbot], chatbot)
    msg.submit(chat_fn, [msg, chatbot], chatbot)
    
demo.launch()
