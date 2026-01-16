from src.ingestion.pdf_loader import PDFLoader

def test_corrupted_pdf_does_not_crash():
    loader = PDFLoader("data/granicus_products.pdf")
    docs = loader.load()

    assert len(docs) == 1
    assert docs[0]["metadata"]["status"] == "failed"
