from fastapi import FastAPI
from pydantic import BaseModel
from src.retrieval.grounded_qa import GroundedQASystem
from src.vectordb.chroma_store import ChromaStore
from src.ingestion.ingest_all import ingest_data

app = FastAPI()
qa = GroundedQASystem()
store = ChromaStore()

class ChatRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup():
    ingest_data()

@app.post("/chat")
def chat(req: ChatRequest):
    return qa.answer(req.question)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stats")
def stats():
    return {"indexed_chunks": store.count()}
