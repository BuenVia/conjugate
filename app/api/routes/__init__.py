from fastapi import APIRouter

from app.api.routes import conjugations, moods, practice, pronouns, tenses, users, verbs

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(verbs.router, prefix="/verbs", tags=["verbs"])
router.include_router(moods.router, prefix="/moods", tags=["moods"])
router.include_router(tenses.router, prefix="/tenses", tags=["tenses"])
router.include_router(conjugations.router, prefix="/conjugations", tags=["conjugations"])
router.include_router(practice.router, prefix="/practice", tags=["practice"])
router.include_router(pronouns.router, prefix="/pronouns", tags=["pronouns"])
