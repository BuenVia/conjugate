from sqlalchemy.orm import Session

from app.repositories import verb as verb_repo
from app.schemas.verb import VerbOut


def list_verbs(db: Session) -> list[VerbOut]:
    verbs = verb_repo.get_all_verbs(db)
    return [VerbOut.model_validate(v) for v in verbs]
