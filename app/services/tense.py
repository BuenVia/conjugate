from sqlalchemy.orm import Session

from app.repositories import tense as tense_repo
from app.schemas.tense import TenseOut


def list_tenses(db: Session) -> list[TenseOut]:
    tenses = tense_repo.get_all_tenses(db)
    return [TenseOut(id=t.id, name=t.name, mood_id=t.mood_id, mood_name=t.mood.name) for t in tenses]
