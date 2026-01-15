import logging
import json
import time
import uuid

class JsonLogger:
    def log(self, request, status, latency, extra=None):
        log = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "level": "INFO",
            "request_id": str(uuid.uuid4()),
            "method": request.method,
            "path": request.url.path,
            "status": status,
            "latency_ms": latency
        }
        if extra:
            log.update(extra)
        print(json.dumps(log))
