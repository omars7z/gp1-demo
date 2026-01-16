import pytest
from app import app
from app import placement_test

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"setup AI Placement Test successfully" in response.data


def test_beginner_level():
    assert placement_test(30) == "Beginner"

def test_intermediate_level():
    assert placement_test(60) == "Intermediate"

def test_advanced_level():
    assert placement_test(90) == "Advanced"
