from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.mood import MoodListResponse
from app.services import mood as mood_service

router = APIRouter()


@router.get("/", response_model=MoodListResponse)
def list_moods(db: Session = Depends(get_db)) -> MoodListResponse:
    return MoodListResponse(data=mood_service.list_moods(db))
