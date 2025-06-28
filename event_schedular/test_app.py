import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_create_event(client):
    res = client.post('/events', json={
        "title": "Test Event",
        "description": "Testing event creation",
        "start_time": "2025-06-29T10:00:00",
        "end_time": "2025-06-29T11:00:00"
    })
    assert res.status_code == 201

def test_list_events(client):
    res = client.get('/events')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)
