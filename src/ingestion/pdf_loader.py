import pdfplumber
from .base_loader import BaseLoader

class PDFLoader(BaseLoader):
    def load_impl(self):
        docs = []

        with pdfplumber.open(self.path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    docs.append({
                        "text": text,
                        "metadata": {
                            "source": self.path,
                            "type": "pdf",
                            "page": i + 1
                        }
                    })
        return docs
