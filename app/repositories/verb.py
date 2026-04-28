from sqlalchemy.orm import Session

from app.models.verb import Verb


def get_all_verbs(db: Session) -> list[Verb]:
    return db.query(Verb).order_by(Verb.id).all()


def get_verbs_by_ids(db: Session, verb_ids: list[int]) -> list[Verb]:
    return db.query(Verb).filter(Verb.id.in_(verb_ids)).all()
