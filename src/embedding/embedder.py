'''
Embedding models options
all-mpnet-base-v2
all-MiniLM-L6-v2
'''

from sentence_transformers import SentenceTransformer
import os

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        cache_dir = os.getenv("MODEL_CACHE_DIR", "models")

        self.model = SentenceTransformer(
            model_name,
            cache_folder=cache_dir
        )

    def embed(self, texts):
        return self.model.encode(texts, show_progress_bar=False)

