from sqlalchemy.orm import Session

from app.repositories import tense as tense_repo
from app.schemas.tense import TenseOut


def list_tenses(db: Session) -> list[TenseOut]:
    tenses = tense_repo.get_all_tenses(db)
    return [TenseOut.model_validate(t) for t in tenses]
