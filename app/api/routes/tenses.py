from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.tense import TenseListResponse
from app.services import tense as tense_service

router = APIRouter()


@router.get("/", response_model=TenseListResponse)
def list_tenses(db: Session = Depends(get_db)) -> TenseListResponse:
    return TenseListResponse(data=tense_service.list_tenses(db))
