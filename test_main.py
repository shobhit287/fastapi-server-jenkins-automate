from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_server_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server running 1.0"}
