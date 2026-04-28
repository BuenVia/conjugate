from sqlalchemy.orm import Session

from app.models.conjugation import Conjugation


def get_conjugations(
    db: Session,
    verb_ids: list[int],
    mood_ids: list[int] | None = None,
    tense_ids: list[int] | None = None,
) -> list[Conjugation]:
    query = db.query(Conjugation).filter(Conjugation.verb_id.in_(verb_ids))
    if mood_ids is not None:
        query = query.filter(Conjugation.mood_id.in_(mood_ids))
    if tense_ids is not None:
        query = query.filter(Conjugation.tense_id.in_(tense_ids))
    return query.all()
