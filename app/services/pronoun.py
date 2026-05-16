from sqlalchemy.orm import Session

from app.repositories import pronoun as pronoun_repo
from app.schemas.pronoun import PronounOut


def list_pronouns(db: Session) -> list[PronounOut]:
    pronouns = pronoun_repo.get_all_pronouns(db)
    return [PronounOut.model_validate(p) for p in pronouns]
