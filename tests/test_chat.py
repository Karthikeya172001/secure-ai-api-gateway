from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def get_token():
    response = client.post(
        "/login",
        data={
            "username": "admin",
            "password": "admin123",
        },
    )
    return response.json()["access_token"]


def test_chat():

    token = get_token()

    response = client.post(
        "/chat",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "prompt": "What is JWT?"
        },
    )

    assert response.status_code in (200, 429)