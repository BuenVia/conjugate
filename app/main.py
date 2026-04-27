from fastapi import FastAPI

from app.api.routes import router
from app.db.base import Base
from app.db.session import engine
from app.models import mood, tense, user, verb  # noqa: F401 — registers ORM models with Base

app = FastAPI(title="LangX API")

app.include_router(router)

Base.metadata.create_all(bind=engine)
