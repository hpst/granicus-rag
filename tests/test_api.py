from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat", json={
        "question": "What products does Granicus offer?"
    })
    assert response.status_code == 200
    assert "answer" in response.json()
