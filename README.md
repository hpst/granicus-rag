# Granicus RAG-Based Chatbot – Data Scientist Case Study

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot for government
technology customer support. The system answers questions **strictly from provided
documents** and refuses out-of-scope queries.

The design emphasizes:
- Grounded responses
- Hallucination prevention
- Enterprise-grade robustness
- Government-friendly security

---

## Architecture

Documents → Ingestion → Chunking → Embeddings → ChromaDB  
User Query → Retrieval → Grounding → Mock LLM → Response

No external LLM APIs are used.

---

## Supported Documents
- PDF (gracefully handles corrupted files)
- CSV (pricing, features, customer segments)
- TXT (FAQs, specs, release notes)
- Markdown & HTML

⚠️ `granicus_products.pdf` is intentionally corrupted and safely skipped.

---



## Docker Setup
```bash
docker build -t granicus-rag .
```

## How To Run
- Start Docker
```bash
docker run --name granicus-api -p 8000:8000 -v $(pwd)/data:/data granicus-rag
```
- go to http://localhost:8000/docs
- Click POST /chat
- Click “Try it out”
- In request body, enter:
```json 
{
  "question": "What products does Granicus offer?"
}
```
- Click Execute
- From terminal
```bash
curl -X 'POST' \
  'http://localhost:8000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "What products does Granicus offer?"
}'
```

## How To Run (DEV)

```bash
python standalone_rag.py
```

## Testing
```bash
python -m pytest tests/ -v
```



