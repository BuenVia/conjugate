from sqlalchemy.orm import Session

from app.models.conjugation import Conjugation

PERSON_ORDER = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]


def get_practice_conjugations(
    db: Session,
    verb_ids: list[int],
    tense_ids: list[int] | None = None,
    pronoun_ids: list[int] | None = None,
) -> list[Conjugation]:
    query = db.query(Conjugation).filter(Conjugation.verb_id.in_(verb_ids))
    if tense_ids is not None:
        query = query.filter(Conjugation.tense_id.in_(tense_ids))
    if pronoun_ids is not None:
        persons = [PERSON_ORDER[i - 1] for i in pronoun_ids if 1 <= i <= len(PERSON_ORDER)]
        if persons:
            query = query.filter(Conjugation.person.in_(persons))
    return query.all()
