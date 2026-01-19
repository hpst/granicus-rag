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

    question_list = ["What are the key features of GovDelivery Communications Cloud?",
                    "What products does Granicus offer for government organizations?",
                    "How much does the Enterprise plan cost for 100,000 subscribers?",
                    "What’s included in the Professional tier pricing?",
                    "What are the API rate limits for different plan tiers?",
                    "What integrations are available with Granicus products?",
                    "What’s the difference between Starter and Professional plans?",
                    "Which plan includes advanced analytics features?"]
    
    #Out-of scope questions for testing
    # question_list = ["What’s the weather like today?",
    #                 "How does Granicus compare to Mailchimp?",
    #                 "What’s the CEO’s personal phone number?",
    #                 "Can you provide customer contact information?",
    #                 "Which Granicus product is the best?",
    #                 "Should I choose Granicus over competitors?"]

    for question in question_list:
        print("\n========QUESTION:", question)

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
