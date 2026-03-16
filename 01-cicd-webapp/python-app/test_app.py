import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello from Python DevOps App!' in rv.data

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert b'healthy' in rv.data

def test_info(client):
    rv = client.get('/info')
    assert rv.status_code == 200
    assert b'Python DevOps App' in rv.data
    assert b'1.0.1' in rv.data
