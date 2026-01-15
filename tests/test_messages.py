from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_and_get_messages():
    # create a manual message
    res = client.post("/messages", json={"content": "manual message"})
    assert res.status_code == 200
    body = res.json()
    assert body.get("status") == "created"
    messages = client.get("/messages").json()
    assert any(m.get("content") == "manual message" for m in messages)
