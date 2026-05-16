from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.db.base import Base
from app.db.session import engine
from app.models import conjugation, mood, pronoun, tense, user, verb  # noqa: F401 — registers ORM models with Base

app = FastAPI(title="LangX API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(router)

Base.metadata.create_all(bind=engine)
