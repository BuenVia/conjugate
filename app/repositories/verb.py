from sqlalchemy.orm import Session

from app.models.verb import Verb


def get_all_verbs(db: Session) -> list[Verb]:
    return db.query(Verb).order_by(Verb.id).all()
