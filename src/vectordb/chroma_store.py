import os
import chromadb
from chromadb.config import Settings

class ChromaStore:
    def __init__(self):
        persist_dir = "/data/chroma_db"
        os.makedirs(persist_dir, exist_ok=True)

        self.client = chromadb.Client(
            Settings(
                persist_directory=persist_dir,
                anonymized_telemetry=False
            )
        )
        self.collection = self.client.get_or_create_collection(
            name="granicus",
            metadata={"hnsw:space": "cosine"}
        )

    def add(self, ids, embeddings, docs, metas):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=docs,
            metadatas=metas
        )

    def query(self, emb, k=5):
        return self.collection.query(query_embeddings=[emb], n_results=k)

    def count(self):
        return self.collection.count()
