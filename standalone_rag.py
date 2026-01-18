# src/standalone_rag.py

import time
from src.ingestion.ingest_all import ingest_data
from src.retrieval.grounded_qa import GroundedQASystem

def main():
    print("=== Running ingestion ===")
    start_ingest = time.time()
    ingest_data(data_dir="data")
    ingest_time = time.time() - start_ingest

    print(f"==== Ingestion completed in {ingest_time:.2f} seconds")

    qa = GroundedQASystem()

    question = "What products does Granicus offer?"
    # question = "What’s the CEO’s personal phone number?"

    print("\nQUESTION:", question)

    start_query = time.time()
    result = qa.answer(question)
    query_time = time.time() - start_query

    print("\nANSWER:")
    print(result["answer"])
    print("\nCONFIDENCE:", result["confidence"])
    print("SOURCES:", result["sources"])

    print(f"\nQuery response time: {query_time:.2f} seconds")

if __name__ == "__main__":
    main()
