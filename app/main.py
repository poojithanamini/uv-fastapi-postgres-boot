from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.items.router import router as items_router

app = FastAPI(title="uv FastAPI Postgres starter", version="0.1.0")
app.include_router(items_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "uv FastAPI Postgres starter"}


@app.get("/health")
def health(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}
