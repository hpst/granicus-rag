import os
from src.llm.mock_llm import MockLLM
from src.llm.local_llm import LocalHFLLM

def get_llm():
    use_local = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"
    if use_local:
        print("INFO:: USING LOCAL LLM")
        return LocalHFLLM()
    print("INFO:: USING MOCK LLM")
    return MockLLM()
