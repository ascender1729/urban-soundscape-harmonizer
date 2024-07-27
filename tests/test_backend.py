from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Urban Soundscape Harmonizer"}
