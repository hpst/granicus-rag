import markdown
from .base_loader import BaseLoader

class MDLoader(BaseLoader):
    def load(self):
        with open(self.path, encoding="utf-8") as f:
            html = markdown.markdown(f.read())
        return [{
            "text": html,
            "metadata": {
                "source": self.path,
                "type": "md"
            }
        }]
