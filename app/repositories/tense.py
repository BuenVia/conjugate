from sqlalchemy.orm import Session, joinedload

from app.models.tense import Tense


def get_all_tenses(db: Session) -> list[Tense]:
    return db.query(Tense).options(joinedload(Tense.mood)).order_by(Tense.id).all()


def get_tenses_by_ids(db: Session, tense_ids: list[int]) -> list[Tense]:
    return db.query(Tense).filter(Tense.id.in_(tense_ids)).all()
