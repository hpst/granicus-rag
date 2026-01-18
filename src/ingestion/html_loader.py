from bs4 import BeautifulSoup
from .base_loader import BaseLoader

class HTMLLoader(BaseLoader):
    def load_impl(self):
        with open(self.path, encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        return [{
            "text": soup.get_text(separator=" "),
            "metadata": {
                "source": self.path,
                "type": "html"
            }
        }]
