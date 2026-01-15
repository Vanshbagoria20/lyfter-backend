from app.database import get_db
from datetime import datetime
import sqlite3

def insert_message(data):
    db = get_db()
    try:
        db.execute("""
        INSERT INTO messages
        (message_id, from_msisdn, to_msisdn, ts, text, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["message_id"],
            data["from"],
            data["to"],
            data["ts"],
            data.get("text"),
            datetime.utcnow().isoformat() + "Z"
        ))
        db.commit()
        return "created"
    except sqlite3.IntegrityError:
        return "duplicate"


def fetch_messages(limit, offset, from_msisdn=None, since=None, q=None):
    db = get_db()
    filters, params = [], []

    if from_msisdn:
        filters.append("from_msisdn = ?")
        params.append(from_msisdn)
    if since:
        filters.append("ts >= ?")
        params.append(since)
    if q:
        filters.append("LOWER(text) LIKE ?")
        params.append(f"%{q.lower()}%")

    where = "WHERE " + " AND ".join(filters) if filters else ""

    total = db.execute(
        f"SELECT COUNT(*) FROM messages {where}",
        params
    ).fetchone()[0]

    rows = db.execute(
        f"""
        SELECT message_id,
               from_msisdn AS "from",
               to_msisdn AS "to",
               ts, text AS content
        FROM messages
        {where}
        ORDER BY ts ASC, message_id ASC
        LIMIT ? OFFSET ?
        """,
        params + [limit, offset]
    ).fetchall()

    return [dict(r) for r in rows], total


def fetch_stats():
    db = get_db()

    total = db.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    senders = db.execute("SELECT COUNT(DISTINCT from_msisdn) FROM messages").fetchone()[0]

    per_sender = db.execute("""
        SELECT from_msisdn AS "from", COUNT(*) AS count
        FROM messages
        GROUP BY from_msisdn
        ORDER BY count DESC
        LIMIT 10
    """).fetchall()

    ts = db.execute("SELECT MIN(ts), MAX(ts) FROM messages").fetchone()

    return {
        "total_messages": total,
        "senders_count": senders,
        "messages_per_sender": [dict(r) for r in per_sender],
        "first_message_ts": ts[0],
        "last_message_ts": ts[1]
    }
