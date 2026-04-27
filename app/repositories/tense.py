from sqlalchemy.orm import Session

from app.models.tense import Tense


def get_all_tenses(db: Session) -> list[Tense]:
    return db.query(Tense).order_by(Tense.id).all()
