from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.pronoun import PronounListResponse
from app.services import pronoun as pronoun_service

router = APIRouter()


@router.get("/", response_model=PronounListResponse)
def list_pronouns(db: Session = Depends(get_db)) -> PronounListResponse:
    return PronounListResponse(data=pronoun_service.list_pronouns(db))
