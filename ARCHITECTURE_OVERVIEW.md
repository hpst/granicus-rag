# Architecture Overview – Granicus RAG Chatbot

## Problem Summary
Design a grounded RAG chatbot for government technology support using multi-format documents.

## High-Level Architecture
Documents → Ingestion → Chunking → Embeddings → ChromaDB
User Query → Retrieval → Grounding → Mock LLM → Response

## Key Design Decisions
- ChromaDB for local vector storage
- Sentence-Transformers for CPU-only embeddings
- Row-wise ingestion for CSV files
- Strict similarity threshold to prevent hallucination
- Mock LLM to enforce deterministic, grounded responses

## Error Handling
- Corrupted documents are isolated and skipped
- Pipeline continues even if individual files fail

## Security Considerations
- No external API calls
- Input validation via FastAPI
- No prompt injection risk

## Testing Strategy
- Unit tests for ingestion & retrieval
- Integration tests for API
- Explicit tests for out-of-scope refusal

## Scalability Notes
- Stateless API
- Vector DB can be swapped with managed services
- LLM layer is pluggable
