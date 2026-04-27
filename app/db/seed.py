from app.db.session import SessionLocal
from app.models.mood import Mood
from app.models.tense import Tense
from app.models.verb import Verb

COMMON_VERBS = [
    "ser", "estar", "haber", "tener", "hacer",
    "poder", "decir", "ir", "ver", "dar",
]

MOODS_AND_TENSES = [
    {
        "name": "Indicative",
        "tenses": [
            "Present",
            "Preterite",
            "Imperfect",
            "Future",
            "Conditional",
            "Present Perfect",
            "Past Perfect",
            "Future Perfect",
            "Conditional Perfect",
        ],
    },
    {
        "name": "Subjunctive",
        "tenses": [
            "Present",
            "Imperfect",
            "Present Perfect",
            "Past Perfect",
            "Future",
        ],
    },
    {
        "name": "Imperative",
        "tenses": [
            "Affirmative",
            "Negative",
        ],
    },
]


def seed_verbs(db) -> None:
    if db.query(Verb).count() > 0:
        print("Verbs already seeded.")
        return
    db.add_all([Verb(infinitive=v) for v in COMMON_VERBS])
    db.commit()
    print(f"Seeded {len(COMMON_VERBS)} verbs.")


def seed_moods_and_tenses(db) -> None:
    if db.query(Mood).count() > 0:
        print("Moods/tenses already seeded.")
        return

    for mood_data in MOODS_AND_TENSES:
        mood = Mood(name=mood_data["name"])
        db.add(mood)
        db.flush()
        db.add_all([Tense(name=t, mood_id=mood.id) for t in mood_data["tenses"]])

    db.commit()
    total_tenses = sum(len(m["tenses"]) for m in MOODS_AND_TENSES)
    print(f"Seeded {len(MOODS_AND_TENSES)} moods and {total_tenses} tenses.")


if __name__ == "__main__":
    from app.db.base import Base
    from app.db.session import engine
    import app.models.mood   # noqa: F401
    import app.models.tense  # noqa: F401
    import app.models.verb   # noqa: F401

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        seed_verbs(db)
        seed_moods_and_tenses(db)
    finally:
        db.close()
