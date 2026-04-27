from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.verb import VerbListResponse
from app.services import verb as verb_service

router = APIRouter()


@router.get("/", response_model=VerbListResponse)
def list_verbs(db: Session = Depends(get_db)) -> VerbListResponse:
    return VerbListResponse(data=verb_service.list_verbs(db))
