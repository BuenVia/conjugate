from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.conjugation import ConjugationErrorResponse, ConjugationResponse
from app.services import conjugation as conjugation_service

router = APIRouter()


@router.get("/", response_model=ConjugationResponse)
def get_conjugations(
    verb: str | None = Query(None),
    mood: str | None = Query(None),
    tense: str | None = Query(None),
    db: Session = Depends(get_db),
):
    if not verb:
        return JSONResponse(
            status_code=400,
            content=ConjugationErrorResponse(
                error={"message": "Query parameter 'verb' is required."}
            ).model_dump(),
        )

    try:
        verb_ids = [int(v.strip()) for v in verb.split(",")]
        mood_ids = [int(m.strip()) for m in mood.split(",")] if mood else None
        tense_ids = [int(t.strip()) for t in tense.split(",")] if tense else None
    except ValueError:
        return JSONResponse(
            status_code=422,
            content=ConjugationErrorResponse(
                error={"message": "IDs must be integers."}
            ).model_dump(),
        )

    try:
        data = conjugation_service.get_conjugations(db, verb_ids, mood_ids, tense_ids)
    except ValueError as e:
        return JSONResponse(
            status_code=404,
            content=ConjugationErrorResponse(
                error={"message": str(e)}
            ).model_dump(),
        )

    return ConjugationResponse(data=data)
