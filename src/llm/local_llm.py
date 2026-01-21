'''
LLM models options:
google/flan-t5-small
google/flan-t5-base
'''

import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class LocalHFLLM:
    """
    Local, CPU-only HuggingFace LLM for grounded answer generation.
    Uses FLAN-T5 style instruction models.
    """

    def __init__(self, model_name="google/flan-t5-base"):
        self.model_name = model_name
        
        self.cache_dir = os.getenv("MODEL_CACHE_DIR", "./models")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=self.cache_dir)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=self.cache_dir)

        self.model.eval()
        self.device = torch.device("cpu")
        self.model.to(self.device)

    def _build_prompt(self, question: str, contexts: list[str]) -> str:
        context_text = "\n\n".join(contexts)

        prompt = f"""
You are a government product assistant.

Answer ONLY using the information below.
If the answer is not contained in the context, say:
"I don’t have sufficient information in the provided documents."

CONTEXT:
{context_text}

QUESTION:
{question}

ANSWER:
""".strip()

        return prompt

    def generate(self, question, context) -> str:
        if not context:
            return {
                "answer": "I don’t have sufficient information in the provided documents.",
                "confidence": 0.05,
                "sources": []
            }
        

        contexts = [c["text"] for c in context[:5]]
        sources = list({c["metadata"]["source"] for c in context[:5]})
        confidence = min(1.0, sum(c["similarity"] for c in context[:5]) / len(context[:5]))

        prompt = self._build_prompt(question, contexts)

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=2048
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.0,
                do_sample=False
            )

        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {
            "answer": answer,
            "confidence": round(confidence, 2),
            "sources": sources
        }