from fastapi.testclient import TestClient

from file_management.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

    response = client.post("/")
    assert response.status_code == 405


def test_manage_file():
    response = client.post("/manage_file", data='{"action":"read"}')
    assert response.json() == {"i_should": "Read"}
    assert response.status_code == 200

    response = client.post("/manage_file", data='{"action":"download"}')
    assert response.json() == {"i_should": "Download"}
    assert response.status_code == 200
