from sqlalchemy.orm import Session

from app.repositories import mood as mood_repo
from app.schemas.mood import MoodOut


def list_moods(db: Session) -> list[MoodOut]:
    moods = mood_repo.get_all_moods(db)
    return [MoodOut.model_validate(m) for m in moods]
