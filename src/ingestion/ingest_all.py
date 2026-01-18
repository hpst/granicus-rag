import os
from .pdf_loader import PDFLoader
from .csv_loader import CSVLoader
from .txt_loader import TXTLoader
from .md_loader import MDLoader
from .html_loader import HTMLLoader
from src.embedding.chunker import TextChunker
from src.embedding.embedder import Embedder
from src.vectordb.chroma_store import ChromaStore
import uuid

LOADERS = {
    ".pdf": PDFLoader,
    ".csv": CSVLoader,
    ".txt": TXTLoader,
    ".md": MDLoader,
    ".html": HTMLLoader,
}

def ingest_data(data_dir="data"):
    chunker = TextChunker()
    embedder = Embedder()
    store = ChromaStore()

    texts, metas, ids = [], [], []

    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)
        ext = os.path.splitext(file)[1].lower()
        if ext not in LOADERS:
            continue

        loader = LOADERS[ext](path)
        docs = loader.load()

        if docs[0]["metadata"].get("status") == "failed":
            print(file, " - failed to load or file currupted: ", docs[0]["metadata"].get("error"))
            continue

        for d in docs:
            for chunk in chunker.chunk(d["text"]):
                texts.append(chunk)
                metas.append(d["metadata"])
                ids.append(str(uuid.uuid4()))
        print(f"{file} - Ingested {len(docs)} documents.")
    if texts:
        store.add(ids, embedder.embed(texts), texts, metas)
