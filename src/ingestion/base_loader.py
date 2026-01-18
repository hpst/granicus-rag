from abc import ABC, abstractmethod

class BaseLoader(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def load_impl(self) -> list[dict]:
        pass
    def load(self) -> list[dict]:
        try:
            return self.load_impl()
        except Exception as e:
            return [{
                "text": "",
                "metadata": {
                    "source": self.path,
                    "status": "failed",
                    "error": str(e)
                }
            }]