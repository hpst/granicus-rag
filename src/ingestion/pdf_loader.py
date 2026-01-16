import pdfplumber
from .base_loader import BaseLoader

class PDFLoader(BaseLoader):
    def load(self):
        docs = []
        try:
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
        except Exception as e:
            return [{
                "text": "",
                "metadata": {
                    "source": self.path,
                    "type": "pdf",
                    "status": "failed",
                    "error": str(e)
                }
            }]
        return docs
