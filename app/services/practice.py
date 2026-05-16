import random

from sqlalchemy.orm import Session

from app.repositories import mood as mood_repo
from app.repositories import practice as practice_repo
from app.repositories import tense as tense_repo
from app.repositories import verb as verb_repo
from app.schemas.practice import PracticeItem


def get_practice(
    db: Session,
    verb_ids: list[int],
    tense_ids: list[int] | None,
    pronoun_ids: list[int] | None,
    limit: int = 20,
) -> list[PracticeItem]:
    verbs = verb_repo.get_verbs_by_ids(db, verb_ids)
    found_ids = {v.id for v in verbs}
    missing = [vid for vid in verb_ids if vid not in found_ids]
    if missing:
        raise ValueError(f"Verb IDs not found: {missing}")

    rows = practice_repo.get_practice_conjugations(db, verb_ids, tense_ids, pronoun_ids)

    verb_map = {v.id: v for v in verbs}
    mood_map = {m.id: m for m in mood_repo.get_moods_by_ids(db, list({r.mood_id for r in rows}))}
    tense_map = {t.id: t for t in tense_repo.get_tenses_by_ids(db, list({r.tense_id for r in rows}))}

    items = [
        PracticeItem(
            id=row.id,
            infinitive=verb_map[row.verb_id].infinitive,
            mood=mood_map[row.mood_id].name,
            tense=tense_map[row.tense_id].name,
            pronoun=row.person,
            conjugation=row.value,
        )
        for row in rows
    ]

    random.shuffle(items)
    return items[:limit]
