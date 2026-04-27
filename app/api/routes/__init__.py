from fastapi import APIRouter

from app.api.routes import moods, tenses, users, verbs

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(verbs.router, prefix="/verbs", tags=["verbs"])
router.include_router(moods.router, prefix="/moods", tags=["moods"])
router.include_router(tenses.router, prefix="/tenses", tags=["tenses"])
