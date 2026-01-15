import sqlite3
from app.config import DATABASE_URL

# keep a single connection per process so tests using in-memory DB share the same
_conn = None

def get_db():
    global _conn
    if _conn is not None:
        return _conn
    path = DATABASE_URL.replace("sqlite:///", "")
    # create a persistent connection for the lifetime of the process
    _conn = sqlite3.connect(path, check_same_thread=False)
    _conn.row_factory = sqlite3.Row
    # ensure schema exists (helps tests using in-memory DB if startup wasn't run)
    _conn.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        message_id TEXT PRIMARY KEY,
        from_msisdn TEXT NOT NULL,
        to_msisdn TEXT NOT NULL,
        ts TEXT NOT NULL,
        text TEXT,
        created_at TEXT NOT NULL
    )
    """)
    _conn.commit()
    return _conn
