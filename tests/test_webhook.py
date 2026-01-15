from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_webhook_creates_message():
    # clear state first
    client.app.dependency_overrides.clear()
    res = client.post("/webhook", json={"content": "hello from webhook"})
    assert res.status_code == 200
    body = res.json()
    assert body.get("status") == "ok"
    messages = client.get("/messages").json()
    assert any(m.get("content") == "hello from webhook" for m in messages)
