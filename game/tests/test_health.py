import pytest

@pytest.mark.django_db
def test_health_endpoint_returns_ok(client):
    response = client.get("/api/health/")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.json() == {"status": "ok"}
