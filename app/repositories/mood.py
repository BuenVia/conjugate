from sqlalchemy.orm import Session

from app.models.mood import Mood


def get_all_moods(db: Session) -> list[Mood]:
    return db.query(Mood).order_by(Mood.id).all()
