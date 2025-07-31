# Directory structure:
# graph_rag_system/
# ├── app.py
# ├── api/
# │   └── server.py
# ├── scripts/
# │   └── populate_graph.py
# ├── graph/
# │   ├── cot_logger.py
# │   ├── graph_query.py
# ├── cache/
# │   └── redis_cache.py
# ├── llm/
# │   ├── rag_chain.py
# │   └── embeddings.py
# ├── data/
# │   └── sample_docs/
# ├── requirements.txt
# ├── README.md
# ├── Dockerfile
# ├── docker-compose.yml
# ├── .env
# └── .gitignore

# === docker-compose.yml ===
version: '3.8'
services:
  neo4j:
    image: neo4j:5
    environment:
      - NEO4J_AUTH=neo4j/password
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4j_data:/data

  redis:
    image: redis:7
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - neo4j
      - redis
    env_file:
      - .env
    command: uvicorn api.server:app --host 0.0.0.0 --port 8000 --reload

volumes:
  neo4j_data:
  redis_data:


# === .env ===
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
REDIS_HOST=redis
REDIS_PORT=6379


# === .gitignore ===
__pycache__/
*.pyc
.env
.idea/
.vscode/
venv/
.DS_Store


# === requirements.txt ===
langchain
openai
redis
neo4j
faiss-cpu
fastapi
uvicorn
python-dotenv


# === README.md ===
# Graph-Based RAG System

A chain-of-thought aware Retrieval-Augmented Generation system using Neo4j + Redis + LangChain + FastAPI.

## Features
- Stores reasoning steps in a Neo4j graph
- Caches final answers in Redis
- FastAPI REST API to interact with the model
- Dockerized for local or production deployment

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/graph-rag-system.git
cd graph-rag-system
docker-compose up --build
```

## API Usage
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is our hiring plan?"}'
```

## Dev Utilities
```bash
python scripts/populate_graph.py  # Insert sample CoT chains
```

## Repo Structure
```
├── api/                  # FastAPI wrapper
├── cache/                # Redis interface
├── graph/                # Neo4j logic (logging + retrieval)
├── llm/                  # LangChain-based embeddings and RAG
├── scripts/              # Developer tools (populate, etc)
├── Dockerfile            # Container image definition
├── docker-compose.yml    # Full stack orchestration
├── .env                  # Environment variables for local dev
```

---

This setup now provides a fully containerized, deployable, and callable system for RAG+CoT hybrid retrieval. You can fork, deploy, and extend this easily.


# === Updated README.md section ===
## Ollama Integration
This project uses [Ollama](https://ollama.com) for local LLM execution.
Make sure you have it installed and the following models pulled:

```bash
ollama pull qwen:0.5b
ollama pull nomic-embed-text
```

The LangChain interface wraps Ollama to serve both embeddings and completions locally.
Ensure your `~/.ollama/config` is properly set or use `.env`.


# === Remove diagram figures from LaTeX patent ===
% Architecture diagrams were removed at author's request
% \section*{System Architecture Visuals}
% \subsection*{High-Level Design (HLD)}
% \begin{figure}[h!]
%   \centering
%   \includegraphics[width=0.9\textwidth]{hld.png}
%   \caption{High-Level Architecture}
% \end{figure}
% \subsection*{Low-Level Design (LLD)}
% \begin{figure}[h!]
%   \centering
%   \includegraphics[width=0.9\textwidth]{lld.png}
%   \caption{Low-Level Architecture}
% \end{figure}


\section*{System Guide for Implementation}

This patent is accompanied by a complete working reference implementation hosted in a GitHub-style project structure. The key modules include:

\begin{itemize}
  \item \textbf{Neo4j Logging:} Logs chain-of-thought sequences as graph nodes and relationships.
  \item \textbf{Redis Caching:} Stores final answers for fast retrieval.
  \item \textbf{LangChain RAG with Ollama:} Uses `OllamaEmbeddings` and `Ollama` for local inference and embedding.
  \item \textbf{API Wrapper:} Provides a FastAPI interface for submitting queries.
  \item \textbf{Graph Population Script:} Seeds Neo4j with example reasoning chains.
  \item \textbf{Docker Compose Stack:} Deploys Neo4j, Redis, and the FastAPI app.
\end{itemize}

Full setup and usage instructions are documented in the included README. The system is designed for enterprise-grade reuse, local model execution, and interpretable AI chain reuse.
