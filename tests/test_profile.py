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


def test_profile():

    token = get_token()

    response = client.get(
        "/profile",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200