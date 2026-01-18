import pandas as pd
from .base_loader import BaseLoader

class CSVLoader(BaseLoader):
    def load_impl(self):
        df = pd.read_csv(self.path)
        docs = []
        for i, row in df.iterrows():
            text = " | ".join([f"{c}: {row[c]}" for c in df.columns])
            docs.append({
                "text": text,
                "metadata": {
                    "source": self.path,
                    "type": "csv",
                    "row": int(i)
                }
            })
        return docs
