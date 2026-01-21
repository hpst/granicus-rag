from .retriever import Retriever
from src.llm.mock_llm import MockLLM
from src.llm import get_llm

class GroundedQASystem:
    def __init__(self):
        self.retriever = Retriever()
        # self.llm = MockLLM()
        self.llm = get_llm()


    def answer(self, question):
        context = self.retriever.retrieve(question)
        return self.llm.generate(question, context)
