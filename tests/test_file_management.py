import os.path

from fastapi.testclient import TestClient

from file_management.main import app, get_sample_file

client = TestClient(app)

# This is not the best testing setup. I do too much manual setup and tear down,
# and I don't make use of temporary directories to isolate state between tests.
# Ideally some thought would be put into a making a test harness that takes care
# of this automatically for each test.
# Hey, at least I know it's bad?


def test_index():
    response = client.get("/", allow_redirects=False)
    assert response.is_redirect
    assert response.headers["location"] == "/docs/"

    response = client.post("/")
    assert response.status_code == 405


def test_manage_file_read():
    # First we need to make sure the file is re-downloaded. This is not clean.
    response = client.post("/manage_file", data='{"action":"download"}')
    # Then we try and read it
    response = client.post("/manage_file", data='{"action":"read"}')
    assert b"Lorem" in response.content
    assert response.status_code == 200


def test_manage_file_download():
    response = client.post("/manage_file", data='{"action":"download"}')
    assert response.json() == {"i_should": "Download"}
    assert response.status_code == 200


def test_get_sample_file():
    # Make sure it's starting from a fresh state
    sample_file = "data/sample-text-file.txt"
    if os.path.exists(sample_file):
        os.remove(sample_file)
    if os.path.exists("data/"):
        os.rmdir("data/")
    # Real developers would use a mock network setup for the test so that the
    # test isn't network-dependant. I would like to learn to do that, but that's
    # not in my time-limit right now
    get_sample_file()
    # This really should be a temp file setup, but time
    assert os.path.exists(sample_file)
    # Instead, let's at least clean it up so the test is accurate.
    # This would be dangerous if the service was the authority for some data,
    # but as it is the data is only transitive.
    os.remove(sample_file)
    os.rmdir("data/")


def test_manage_file_errors():
    response = client.post("/manage_file", data='{"action":"make bacon"}')
    assert response.status_code == 422  # 422 = Unprocessable Entity

    response = client.get("/manage_file")
    assert response.status_code == 405  # 405 = Method Not Allowed
