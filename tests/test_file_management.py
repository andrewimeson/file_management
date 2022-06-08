import os.path

from fastapi.testclient import TestClient

from file_management.main import app, get_sample_file

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

    response = client.post("/")
    assert response.status_code == 405


def test_manage_file_read():
    response = client.post("/manage_file", data='{"action":"read"}')
    assert response.json() == {"i_should": "Read"}
    assert response.status_code == 200


def test_manage_file_download():
    response = client.post("/manage_file", data='{"action":"download"}')
    assert response.json() == {"i_should": "Download"}
    assert response.status_code == 200


def test_get_sample_file():
    get_sample_file()
    sample_file = "data/sample-text-file.txt"
    # This really should be a temp file setup, but time
    assert os.path.exists(sample_file)
    # Instead, let's at least clean it up so the test is accurate.
    # This would be dangerous if the service was the authority for some data,
    # but as it is the data is only transitive.
    os.remove(sample_file)
    os.rmdir("data/")
