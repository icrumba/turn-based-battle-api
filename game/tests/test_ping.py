import pytest

@pytest.mark.django_db
def test_ping_endpoint_returns_pong(client):
    response = client.get("/api/ping/")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.json() == {"message": "pong"}
