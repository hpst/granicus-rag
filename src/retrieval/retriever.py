from src.embedding.embedder import Embedder
from src.vectordb.chroma_store import ChromaStore

class Retriever:
    def __init__(self, threshold=0.35):
        self.embedder = Embedder()
        self.store = ChromaStore()
        self.threshold = threshold

    def retrieve(self, question):
        emb = self.embedder.embed([question])[0]
        res = self.store.query(emb)

        docs = []
        for doc, meta, dist in zip(
            res["documents"][0],
            res["metadatas"][0],
            res["distances"][0]
        ):
            sim = 1 - dist
            if sim >= self.threshold:
                docs.append({
                    "text": doc,
                    "metadata": meta,
                    "similarity": sim
                })
        return docs
