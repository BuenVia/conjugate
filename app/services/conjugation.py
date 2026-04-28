from collections import defaultdict

from sqlalchemy.orm import Session

from app.repositories import conjugation as conjugation_repo
from app.repositories import mood as mood_repo
from app.repositories import tense as tense_repo
from app.repositories import verb as verb_repo
from app.schemas.conjugation import MoodOut, PersonConjugation, TenseOut, VerbConjugationOut, VerbOut

PERSON_ORDER = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]


def get_conjugations(
    db: Session,
    verb_ids: list[int],
    mood_ids: list[int] | None,
    tense_ids: list[int] | None,
) -> list[VerbConjugationOut]:
    verbs = verb_repo.get_verbs_by_ids(db, verb_ids)
    found_ids = {v.id for v in verbs}
    missing = [vid for vid in verb_ids if vid not in found_ids]
    if missing:
        raise ValueError(f"Verb IDs not found: {missing}")

    rows = conjugation_repo.get_conjugations(db, verb_ids, mood_ids, tense_ids)

    mood_map = {m.id: m for m in mood_repo.get_moods_by_ids(db, list({r.mood_id for r in rows}))}
    tense_map = {t.id: t for t in tense_repo.get_tenses_by_ids(db, list({r.tense_id for r in rows}))}
    verb_map = {v.id: v for v in verbs}

    # Group: verb_id -> mood_id -> tense_id -> [(person, value)]
    grouped: dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for r in rows:
        grouped[r.verb_id][r.mood_id][r.tense_id].append((r.person, r.value))

    result = []
    for verb_id in verb_ids:
        moods_out = []
        for mood_id, tenses_dict in grouped[verb_id].items():
            tenses_out = []
            for tense_id, persons in tenses_dict.items():
                sorted_persons = sorted(
                    persons,
                    key=lambda x: PERSON_ORDER.index(x[0]) if x[0] in PERSON_ORDER else 999,
                )
                tenses_out.append(TenseOut(
                    id=tense_id,
                    name=tense_map[tense_id].name,
                    conjugations=[PersonConjugation(person=p, value=v) for p, v in sorted_persons],
                ))
            moods_out.append(MoodOut(id=mood_id, name=mood_map[mood_id].name, tenses=tenses_out))
        result.append(VerbConjugationOut(
            verb=VerbOut(id=verb_id, infinitive=verb_map[verb_id].infinitive),
            moods=moods_out,
        ))

    return result
