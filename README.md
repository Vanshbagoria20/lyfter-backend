# Lyftr AI -- Backend Assignment

## Containerized Webhook API

This repository contains a **production-style FastAPI backend service**
built as part of the **Lyftr AI Backend Assignment**.\
The service ingests WhatsApp-like webhook messages **exactly once**,
validates requests using **HMAC-SHA256 signatures**, provides
**queryable message storage**, exposes **analytics**, **health probes**,
**metrics**, and runs fully containerized using **Docker Compose** with
**SQLite** as the database.

------------------------------------------------------------------------

## 🚀 Features Implemented

-   ✅ Secure webhook ingestion with **HMAC-SHA256 verification**
-   ✅ **Exactly-once (idempotent)** message processing
-   ✅ SQLite persistence with Docker volume
-   ✅ Paginated & filterable `/messages` endpoint
-   ✅ Analytical `/stats` endpoint
-   ✅ Health probes (`/health/live`, `/health/ready`)
-   ✅ Prometheus-style `/metrics` endpoint
-   ✅ Structured **JSON logs** (one line per request)
-   ✅ 12-factor configuration via environment variables
-   ✅ Dockerized deployment

------------------------------------------------------------------------

## 🧱 Tech Stack

-   **Language:** Python 3.11\
-   **Framework:** FastAPI\
-   **Database:** SQLite\
-   **Containerization:** Docker, Docker Compose\
-   **Logging:** Structured JSON logs\
-   **Metrics:** Prometheus-style text format

------------------------------------------------------------------------

## 📁 Project Structure

    app/
     ├── main.py          # FastAPI app and routes
     ├── config.py        # Environment configuration
     ├── database.py      # SQLite connection
     ├── models.py        # DB schema initialization
     ├── storage.py       # Database operations
     ├── logging_utils.py # Structured JSON logging
     ├── metrics.py       # Metrics helpers
    Dockerfile
    docker-compose.yml
    Makefile
    README.md

------------------------------------------------------------------------

## ⚙️ Configuration (Environment Variables)

The application follows **12-factor app principles**.\
All configuration is provided via environment variables.

  -----------------------------------------------------------------------
  Variable                     Description
  ---------------------------- ------------------------------------------
  `DATABASE_URL`               SQLite database path
                               (e.g. `sqlite:////data/app.db`)

  `WEBHOOK_SECRET`             Shared secret used for HMAC verification

  `LOG_LEVEL`                  Log level (`INFO`, `DEBUG`)
  -----------------------------------------------------------------------

⚠️ **Important:**\
If `WEBHOOK_SECRET` is not set, the application **will not become
ready**.

------------------------------------------------------------------------

## ▶️ How to Run the Application

### Prerequisites

-   Docker
-   Docker Compose
-   Make (optional but recommended)

### Start the application

``` bash
make up
```

or:

``` bash
docker compose up -d --build
```

API base URL:

    http://localhost:8000

### Stop the application

``` bash
make down
```

------------------------------------------------------------------------

## 🔍 API Endpoints

### POST `/webhook`

Securely ingests messages exactly once using HMAC verification.

### GET `/messages`

Lists stored messages with pagination and filters.

### GET `/stats`

Returns message-level analytics.

### Health Checks

-   `/health/live`
-   `/health/ready`

### GET `/metrics`

Prometheus-style metrics endpoint.

------------------------------------------------------------------------

## 🪵 Structured Logging

-   One JSON log line per request
-   Includes request metadata, latency, and webhook-specific fields

------------------------------------------------------------------------

## 🔐 Design Decisions

### HMAC Verification

-   Uses raw request body
-   Secure comparison with `hmac.compare_digest`

### Idempotency

-   Enforced via `PRIMARY KEY (message_id)`
-   Duplicate messages handled gracefully

### Pagination

-   Implemented using `LIMIT` and `OFFSET`
-   Accurate `total` count

### Stats

-   SQL aggregation for efficiency

------------------------------------------------------------------------

## 🧠 Setup Used

-   **IDE:** VS Code + Cursor
-   **AI Assistance:** ChatGPT + Gemini 

