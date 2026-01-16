from src.retrieval.grounded_qa import GroundedQASystem

def test_out_of_scope_question_refused():
    qa = GroundedQASystem()
    res = qa.answer("What is the weather today?")
    assert "don’t have sufficient information" in res["answer"]
    assert res["confidence"] < 0.1
