from app import app

def test_home_status_code():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200

def test_home_content():
    client = app.test_client()
    resp = client.get("/")
    assert b"Hello from Flask!" in resp.data
