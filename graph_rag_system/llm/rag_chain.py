from langchain.chains import RetrievalQA
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama

def generate_with_rag(query):
    retriever = FAISS.load_local("index", OllamaEmbeddings(model="nomic-embed-text")).as_retriever()
    rag_chain = RetrievalQA.from_chain_type(llm=Ollama(model="qwen:0.5b"), retriever=retriever)
    answer = rag_chain.run(query)
    reasoning_chain = [
        "Step 1: Embed query with nomic",
        "Step 2: Retrieve documents from FAISS",
        "Step 3: Generate answer via Ollama (Qwen 0.5b)"
    ]
    return reasoning_chain, answer
