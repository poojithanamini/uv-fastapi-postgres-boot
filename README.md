# uv FastAPI PostgreSQL starter

A small FastAPI application managed by [uv](https://docs.astral.sh/uv/), following the straightforward `app/` layout from Astral's `uv-fastapi-example`, plus PostgreSQL, SQLAlchemy, and Alembic.

## Run locally

```bash
cp .env.example .env
docker compose up -d db
uv sync --all-groups
uv run alembic upgrade head
uv run fastapi dev app/main.py
```

Open <http://127.0.0.1:8000/docs>. The database-aware health endpoint is at `/health` and the sample resource is at `/items`.

## Run everything in Docker

```bash
docker compose up --build
docker compose exec api uv run alembic upgrade head
```

## Common commands

```bash
uv run pytest
uv run ruff check .
uv run alembic revision --autogenerate -m "describe change"
uv run alembic upgrade head
```

`DATABASE_URL` defaults to a local PostgreSQL instance; override it in `.env` or the environment. Docker uses the `db` service hostname automatically.

## Layout

```
app/
├── core/       # configuration shared across features
├── db/         # engine, sessions, and SQLAlchemy base
├── items/      # item model, request/response schemas, and routes
└── main.py     # FastAPI application and router registration
```

Add each new domain as its own feature folder (for example, `app/users/`), then register its router in `main.py`.
