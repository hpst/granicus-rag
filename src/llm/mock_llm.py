import math

class MockLLM:
    def generate(self, question, context):
        # print(context, "<<< context in MockLLM")
        if not context:
            return {
                "answer": "I don’t have sufficient information in the provided documents.",
                "confidence": 0.05,
                "sources": []
            }

        answer = context[0]["text"][:400]
        sources = list({c["metadata"]["source"] for c in context})
        confidence = min(1.0, sum(c["similarity"] for c in context) / len(context))

        return {
            "answer": answer,
            "confidence": round(confidence, 2),
            "sources": sources
        }
