import pytest
from quizzes.app import app


@pytest.fixture()
def client():
    return app.test_client()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to this project!' in response.data
    assert b"Sign out is under" in response.data
    assert b"Quizzes v1.0" in response.data


def test_home_page_post(client):
    response = client.post('/')
    assert response.status_code == 405
    assert b'Method Not Allowed' in response.data


def test_choose_quiz_difficulty_route(client):
    response = client.get('/quiz')
    assert response.status_code == 302
    assert b'Redirecting...' in response.data
