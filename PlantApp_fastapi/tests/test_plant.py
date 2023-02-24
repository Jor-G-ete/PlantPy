from fastapi.testclient import TestClient
from PlantApp_fastapi.main import app

test_client = TestClient(app)

def test_plant_creation():
    test_response = test_client.get("/plant")
    assert 1 == test_response.json(), "The value from test response must be 1"