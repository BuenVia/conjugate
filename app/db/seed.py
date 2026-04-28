from app.db.session import SessionLocal
from app.models.mood import Mood
from app.models.tense import Tense
from app.models.verb import Verb
from app.models.conjugation import Conjugation

COMMON_VERBS = [
    "ser", "estar", "haber", "tener", "hacer",
    "poder", "decir", "ir", "ver", "dar",
    "saber", "querer", "llegar", "pasar", "deber",
    "poner", "parecer", "quedar", "creer", "hablar",
    "llevar", "dejar", "seguir", "encontrar", "llamar",
    "venir", "pensar", "salir", "volver", "tomar",
    "conocer", "vivir", "sentir", "tratar", "mirar",
    "contar", "empezar", "esperar", "buscar", "existir",
    "entrar", "trabajar", "escribir", "perder", "producir",
    "ocurrir", "entender", "pedir", "recibir", "recordar",
    "terminar", "permitir", "aparecer", "conseguir", "comenzar",
    "servir", "sacar", "necesitar", "mantener", "resultar",
    "leer", "caer", "cambiar", "presentar", "crear",
    "abrir", "considerar", "oír", "ganar", "formar",
    "traer", "partir", "morir", "aceptar", "realizar",
    "suponer", "comprender", "lograr", "explicar", "preguntar",
    "tocar", "reconocer", "estudiar", "alcanzar", "nacer",
    "dirigir", "correr", "utilizar", "pagar", "ayudar",
    "gustar", "jugar", "escuchar", "cumplir", "ofrecer",
    "descubrir", "levantar", "intentar", "usar", "comprar",
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

PERSONS = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]

CONJUGATION_DATA = {
    "ser": {
        "Indicative": {
            "Present": ["soy", "eres", "es", "somos", "sois", "son"],
            "Preterite": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
            "Imperfect": ["era", "eras", "era", "éramos", "erais", "eran"],
            "Future": ["seré", "serás", "será", "seremos", "seréis", "serán"],
            "Conditional": ["sería", "serías", "sería", "seríamos", "seríais", "serían"],
            "Present Perfect": ["he sido", "has sido", "ha sido", "hemos sido", "habéis sido", "han sido"],
            "Past Perfect": ["había sido", "habías sido", "había sido", "habíamos sido", "habíais sido", "habían sido"],
            "Future Perfect": ["habré sido", "habrás sido", "habrá sido", "habremos sido", "habréis sido", "habrán sido"],
            "Conditional Perfect": ["habría sido", "habrías sido", "habría sido", "habríamos sido", "habríais sido", "habrían sido"],
        },
        "Subjunctive": {
            "Present": ["sea", "seas", "sea", "seamos", "seáis", "sean"],
            "Imperfect": ["fuera", "fueras", "fuera", "fuéramos", "fuerais", "fueran"],
            "Present Perfect": ["haya sido", "hayas sido", "haya sido", "hayamos sido", "hayáis sido", "hayan sido"],
            "Past Perfect": ["hubiera sido", "hubieras sido", "hubiera sido", "hubiéramos sido", "hubierais sido", "hubieran sido"],
            "Future": ["fuere", "fueres", "fuere", "fuéremos", "fuereis", "fueren"],
        },
        "Imperative": {
            "Affirmative": ["-", "sé", "sea", "seamos", "sed", "sean"],
            "Negative": ["-", "no seas", "no sea", "no seamos", "no seáis", "no sean"],
        },
    },
    "estar": {
        "Indicative": {
            "Present": ["estoy", "estás", "está", "estamos", "estáis", "están"],
            "Preterite": ["estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"],
            "Imperfect": ["estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"],
            "Future": ["estaré", "estarás", "estará", "estaremos", "estaréis", "estarán"],
            "Conditional": ["estaría", "estarías", "estaría", "estaríamos", "estaríais", "estarían"],
            "Present Perfect": ["he estado", "has estado", "ha estado", "hemos estado", "habéis estado", "han estado"],
            "Past Perfect": ["había estado", "habías estado", "había estado", "habíamos estado", "habíais estado", "habían estado"],
            "Future Perfect": ["habré estado", "habrás estado", "habrá estado", "habremos estado", "habréis estado", "habrán estado"],
            "Conditional Perfect": ["habría estado", "habrías estado", "habría estado", "habríamos estado", "habríais estado", "habrían estado"],
        },
        "Subjunctive": {
            "Present": ["esté", "estés", "esté", "estemos", "estéis", "estén"],
            "Imperfect": ["estuviera", "estuvieras", "estuviera", "estuviéramos", "estuvierais", "estuvieran"],
            "Present Perfect": ["haya estado", "hayas estado", "haya estado", "hayamos estado", "hayáis estado", "hayan estado"],
            "Past Perfect": ["hubiera estado", "hubieras estado", "hubiera estado", "hubiéramos estado", "hubierais estado", "hubieran estado"],
            "Future": ["estuviere", "estuvieres", "estuviere", "estuviéremos", "estuviereis", "estuvieren"],
        },
        "Imperative": {
            "Affirmative": ["-", "está", "esté", "estemos", "estad", "estén"],
            "Negative": ["-", "no estés", "no esté", "no estemos", "no estéis", "no estén"],
        },
    },
    "haber": {
        "Indicative": {
            "Present": ["he", "has", "ha", "hemos", "habéis", "han"],
            "Preterite": ["hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron"],
            "Imperfect": ["había", "habías", "había", "habíamos", "habíais", "habían"],
            "Future": ["habré", "habrás", "habrá", "habremos", "habréis", "habrán"],
            "Conditional": ["habría", "habrías", "habría", "habríamos", "habríais", "habrían"],
            "Present Perfect": ["he habido", "has habido", "ha habido", "hemos habido", "habéis habido", "han habido"],
            "Past Perfect": ["había habido", "habías habido", "había habido", "habíamos habido", "habíais habido", "habían habido"],
            "Future Perfect": ["habré habido", "habrás habido", "habrá habido", "habremos habido", "habréis habido", "habrán habido"],
            "Conditional Perfect": ["habría habido", "habrías habido", "habría habido", "habríamos habido", "habríais habido", "habrían habido"],
        },
        "Subjunctive": {
            "Present": ["haya", "hayas", "haya", "hayamos", "hayáis", "hayan"],
            "Imperfect": ["hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"],
            "Present Perfect": ["haya habido", "hayas habido", "haya habido", "hayamos habido", "hayáis habido", "hayan habido"],
            "Past Perfect": ["hubiera habido", "hubieras habido", "hubiera habido", "hubiéramos habido", "hubierais habido", "hubieran habido"],
            "Future": ["hubiere", "hubieres", "hubiere", "hubiéremos", "hubiereis", "hubieren"],
        },
        "Imperative": {
            "Affirmative": ["-", "he", "haya", "hayamos", "habed", "hayan"],
            "Negative": ["-", "no hayas", "no haya", "no hayamos", "no hayáis", "no hayan"],
        },
    },
    "tener": {
        "Indicative": {
            "Present": ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"],
            "Preterite": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
            "Imperfect": ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
            "Future": ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"],
            "Conditional": ["tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"],
            "Present Perfect": ["he tenido", "has tenido", "ha tenido", "hemos tenido", "habéis tenido", "han tenido"],
            "Past Perfect": ["había tenido", "habías tenido", "había tenido", "habíamos tenido", "habíais tenido", "habían tenido"],
            "Future Perfect": ["habré tenido", "habrás tenido", "habrá tenido", "habremos tenido", "habréis tenido", "habrán tenido"],
            "Conditional Perfect": ["habría tenido", "habrías tenido", "habría tenido", "habríamos tenido", "habríais tenido", "habrían tenido"],
        },
        "Subjunctive": {
            "Present": ["tenga", "tengas", "tenga", "tengamos", "tengáis", "tengan"],
            "Imperfect": ["tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran"],
            "Present Perfect": ["haya tenido", "hayas tenido", "haya tenido", "hayamos tenido", "hayáis tenido", "hayan tenido"],
            "Past Perfect": ["hubiera tenido", "hubieras tenido", "hubiera tenido", "hubiéramos tenido", "hubierais tenido", "hubieran tenido"],
            "Future": ["tuviere", "tuvieres", "tuviere", "tuviéremos", "tuviereis", "tuvieren"],
        },
        "Imperative": {
            "Affirmative": ["-", "ten", "tenga", "tengamos", "tened", "tengan"],
            "Negative": ["-", "no tengas", "no tenga", "no tengamos", "no tengáis", "no tengan"],
        },
    },
    "hacer": {
        "Indicative": {
            "Present": ["hago", "haces", "hace", "hacemos", "hacéis", "hacen"],
            "Preterite": ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"],
            "Imperfect": ["hacía", "hacías", "hacía", "hacíamos", "hacíais", "hacían"],
            "Future": ["haré", "harás", "hará", "haremos", "haréis", "harán"],
            "Conditional": ["haría", "harías", "haría", "haríamos", "haríais", "harían"],
            "Present Perfect": ["he hecho", "has hecho", "ha hecho", "hemos hecho", "habéis hecho", "han hecho"],
            "Past Perfect": ["había hecho", "habías hecho", "había hecho", "habíamos hecho", "habíais hecho", "habían hecho"],
            "Future Perfect": ["habré hecho", "habrás hecho", "habrá hecho", "habremos hecho", "habréis hecho", "habrán hecho"],
            "Conditional Perfect": ["habría hecho", "habrías hecho", "habría hecho", "habríamos hecho", "habríais hecho", "habrían hecho"],
        },
        "Subjunctive": {
            "Present": ["haga", "hagas", "haga", "hagamos", "hagáis", "hagan"],
            "Imperfect": ["hiciera", "hicieras", "hiciera", "hiciéramos", "hicierais", "hicieran"],
            "Present Perfect": ["haya hecho", "hayas hecho", "haya hecho", "hayamos hecho", "hayáis hecho", "hayan hecho"],
            "Past Perfect": ["hubiera hecho", "hubieras hecho", "hubiera hecho", "hubiéramos hecho", "hubierais hecho", "hubieran hecho"],
            "Future": ["hiciere", "hicieres", "hiciere", "hiciéremos", "hiciereis", "hicieren"],
        },
        "Imperative": {
            "Affirmative": ["-", "haz", "haga", "hagamos", "haced", "hagan"],
            "Negative": ["-", "no hagas", "no haga", "no hagamos", "no hagáis", "no hagan"],
        },
    },
}


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


def seed_conjugations(db) -> None:
    if db.query(Conjugation).count() > 0:
        print("Conjugations already seeded.")
        return

    total = 0
    for verb_infinitive, moods_data in CONJUGATION_DATA.items():
        verb = db.query(Verb).filter(Verb.infinitive == verb_infinitive).first()
        if not verb:
            print(f"Verb '{verb_infinitive}' not found, skipping.")
            continue

        for mood_name, tenses_data in moods_data.items():
            mood = db.query(Mood).filter(Mood.name == mood_name).first()
            if not mood:
                print(f"Mood '{mood_name}' not found, skipping.")
                continue

            for tense_name, forms in tenses_data.items():
                tense = db.query(Tense).filter(
                    Tense.name == tense_name,
                    Tense.mood_id == mood.id,
                ).first()
                if not tense:
                    print(f"Tense '{tense_name}' not found, skipping.")
                    continue

                for person, value in zip(PERSONS, forms):
                    db.add(Conjugation(
                        verb_id=verb.id,
                        mood_id=mood.id,
                        tense_id=tense.id,
                        person=person,
                        value=value,
                    ))
                    total += 1

    db.commit()
    print(f"Seeded {total} conjugations.")


if __name__ == "__main__":
    from app.db.base import Base
    from app.db.session import engine
    import app.models.mood        # noqa: F401
    import app.models.tense       # noqa: F401
    import app.models.verb        # noqa: F401
    import app.models.conjugation # noqa: F401

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        seed_verbs(db)
        seed_moods_and_tenses(db)
        seed_conjugations(db)
    finally:
        db.close()
