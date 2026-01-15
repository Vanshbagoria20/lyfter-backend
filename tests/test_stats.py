from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_stats_counters():
    # initial
    stats0 = client.get("/stats").json()
    assert isinstance(stats0, dict)
    # trigger events
    client.post("/webhook", json={"content": "s1"})
    client.post("/messages", json={"content": "s2"})
    stats = client.get("/stats").json()
    assert stats.get("webhook_events", 0) >= 1
    assert stats.get("messages_created", 0) >= 1
