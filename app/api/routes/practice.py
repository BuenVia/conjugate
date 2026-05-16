from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.practice import PracticeErrorResponse, PracticeResponse
from app.services import practice as practice_service

router = APIRouter()


@router.get("/", response_model=PracticeResponse)
def get_practice(
    verbs: str | None = Query(None),
    tenses: str | None = Query(None),
    pronouns: str | None = Query(None),
    db: Session = Depends(get_db),
):
    if not verbs:
        return JSONResponse(
            status_code=400,
            content=PracticeErrorResponse(
                error={"message": "Query parameter 'verbs' is required."}
            ).model_dump(),
        )

    try:
        verb_ids = [int(v.strip()) for v in verbs.split(",")]
        tense_ids = [int(t.strip()) for t in tenses.split(",")] if tenses else None
        pronoun_ids = [int(p.strip()) for p in pronouns.split(",")] if pronouns else None
    except ValueError:
        return JSONResponse(
            status_code=422,
            content=PracticeErrorResponse(
                error={"message": "IDs must be integers."}
            ).model_dump(),
        )

    try:
        data = practice_service.get_practice(db, verb_ids, tense_ids, pronoun_ids)
    except ValueError as e:
        return JSONResponse(
            status_code=404,
            content=PracticeErrorResponse(
                error={"message": str(e)}
            ).model_dump(),
        )

    return PracticeResponse(data=data)
