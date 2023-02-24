from main import app
from fastapi.testclient import TestClient


test_client = TestClient(app)

def test_plant_creation():
    test_response  = test_client.get("/plant")
    assert 1 == test_response , "The value from test response must be 1"