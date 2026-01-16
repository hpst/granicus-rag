from abc import ABC, abstractmethod

class BaseLoader(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def load(self) -> list[dict]:
        pass
