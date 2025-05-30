import pytest
from web_ui.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"AI Security Assistant" in response.data or b"<html" in response.data

def test_scan_endpoint(client):
    response = client.post('/scan', json={"targets": ["127.0.0.1"]})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "status" in json_data
    assert json_data["status"] == "scanning started"
    assert "targets" in json_data
    assert "127.0.0.1" in json_data["targets"]
