from sqlalchemy.orm import Session

from app.models.pronoun import Pronoun


def get_all_pronouns(db: Session) -> list[Pronoun]:
    return db.query(Pronoun).order_by(Pronoun.id).all()
