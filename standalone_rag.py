"""
Standalone RAG test script.
Runs ingestion, embedding, retrieval, and prints answer to terminal.
"""

import os
import uuid
from src.ingestion.csv_loader import CSVLoader
from src.ingestion.txt_loader import TXTLoader
from src.ingestion.md_loader import MDLoader
from src.ingestion.html_loader import HTMLLoader
from src.ingestion.pdf_loader import PDFLoader

from src.embedding.chunker import TextChunker
from src.embedding.embedder import Embedder
from src.vectordb.chroma_store import ChromaStore


DATA_DIR = "data"


def load_documents():
    docs = []

    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)
        ext = os.path.splitext(file)[1].lower()
        print(file)
        try:
            if ext == ".csv":
                docs.extend(CSVLoader(path).load())
            elif ext == ".txt":
                docs.extend(TXTLoader(path).load())
            elif ext == ".md":
                docs.extend(MDLoader(path).load())
            elif ext == ".html":
                docs.extend(HTMLLoader(path).load())
            elif ext == ".pdf":
                docs.extend(PDFLoader(path).load())
        except Exception as e:
            print(f"[SKIP] {file} → {e}")

    return docs


def ingest():
    print("\n=== INGESTION STARTED ===")

    docs = load_documents()
    chunker = TextChunker()
    embedder = Embedder()
    store = ChromaStore()

    texts, metas, ids = [], [], []

    for d in docs:
        if d["metadata"].get("status") == "failed":
            continue

        chunks = chunker.chunk(d["text"])
        for c in chunks:
            texts.append(c)
            metas.append(d["metadata"])
            ids.append(str(uuid.uuid4()))

    print(f"Total chunks: {len(texts)}")

    embeddings = embedder.embed(texts)
    store.add(ids, embeddings, texts, metas)

    print("=== INGESTION COMPLETE ===")
    print("Stored chunks:", store.count())


def ask_question(question: str):
    print("\n=== QUESTION ===")
    print(question)

    embedder = Embedder()
    store = ChromaStore()

    q_embedding = embedder.embed([question])[0]
    results = store.query(q_embedding, k=5)

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]

    if not docs:
        print("\nNo relevant documents found.")
        return

    print("\n=== ANSWER (EXTRACTED CONTEXT) ===")
    for i, (doc, meta, dist) in enumerate(zip(docs, metas, distances), 1):
        similarity = round(1 - dist, 3)
        print(f"\n--- Result {i} (similarity={similarity}) ---")
        print(doc[:500])
        print(f"Source: {meta.get('source')}")


if __name__ == "__main__":
    ingest()

    # 👇 CHANGE QUESTION HERE
    question = "What products does Granicus offer?"

    ask_question(question)
