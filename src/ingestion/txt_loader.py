from .base_loader import BaseLoader

class TXTLoader(BaseLoader):
    def load(self):
        with open(self.path, encoding="utf-8") as f:
            return [{
                "text": f.read(),
                "metadata": {
                    "source": self.path,
                    "type": "txt"
                }
            }]
