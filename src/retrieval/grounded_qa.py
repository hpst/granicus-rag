from .retriever import Retriever
from src.llm.mock_llm import MockLLM

class GroundedQASystem:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = MockLLM()

    def answer(self, question):
        context = self.retriever.retrieve(question)
        return self.llm.generate(question, context)
