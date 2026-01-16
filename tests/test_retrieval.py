from src.retrieval.retriever import Retriever

def test_retrieval_returns_list():
    retriever = Retriever()
    docs = retriever.retrieve("What products does Granicus offer?")
    assert isinstance(docs, list)
