from sqlalchemy.orm import Session

from app.models.mood import Mood


def get_all_moods(db: Session) -> list[Mood]:
    return db.query(Mood).order_by(Mood.id).all()


def get_moods_by_ids(db: Session, mood_ids: list[int]) -> list[Mood]:
    return db.query(Mood).filter(Mood.id.in_(mood_ids)).all()
