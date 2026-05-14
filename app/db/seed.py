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
        "name": "Indicativo",
        "tenses": [
            "Presente",
            "Pretérito Indefinido",
            "Pretérito Imperfecto",
            "Futuro Simple",
            "Condicional Simple",
            "Pretérito Perfecto Compuesto",
            "Pretérito Pluscuamperfecto",
            "Futuro Compuesto",
            "Condicional Compuesto",
        ],
    },
    {
        "name": "Subjuntivo",
        "tenses": [
            "Presente",
            "Pretérito Imperfecto",
            "Pretérito Perfecto Compuesto",
            "Pretérito Pluscuamperfecto",
            "Futuro Simple",
        ],
    },
    {
        "name": "Imperativo",
        "tenses": [
            "Afirmativo",
            "Negativo",
        ],
    },
]

PERSONS = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]

CONJUGATION_DATA = {
    "ser": {
        "Indicativo": {
            "Presente": ["soy", "eres", "es", "somos", "sois", "son"],
            "Pretérito Indefinido": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
            "Pretérito Imperfecto": ["era", "eras", "era", "éramos", "erais", "eran"],
            "Futuro Simple": ["seré", "serás", "será", "seremos", "seréis", "serán"],
            "Condicional Simple": ["sería", "serías", "sería", "seríamos", "seríais", "serían"],
            "Pretérito Perfecto Compuesto": ["he sido", "has sido", "ha sido", "hemos sido", "habéis sido", "han sido"],
            "Pretérito Pluscuamperfecto": ["había sido", "habías sido", "había sido", "habíamos sido", "habíais sido", "habían sido"],
            "Futuro Compuesto": ["habré sido", "habrás sido", "habrá sido", "habremos sido", "habréis sido", "habrán sido"],
            "Condicional Compuesto": ["habría sido", "habrías sido", "habría sido", "habríamos sido", "habríais sido", "habrían sido"],
        },
        "Subjuntivo": {
            "Presente": ["sea", "seas", "sea", "seamos", "seáis", "sean"],
            "Pretérito Imperfecto": ["fuera", "fueras", "fuera", "fuéramos", "fuerais", "fueran"],
            "Pretérito Perfecto Compuesto": ["haya sido", "hayas sido", "haya sido", "hayamos sido", "hayáis sido", "hayan sido"],
            "Pretérito Pluscuamperfecto": ["hubiera sido", "hubieras sido", "hubiera sido", "hubiéramos sido", "hubierais sido", "hubieran sido"],
            "Futuro Simple": ["fuere", "fueres", "fuere", "fuéremos", "fuereis", "fueren"],
        },
        "Imperativo": {
            "Afirmativo": ["-", "sé", "sea", "seamos", "sed", "sean"],
            "Negativo": ["-", "no seas", "no sea", "no seamos", "no seáis", "no sean"],
        },
    },
    "estar": {
        "Indicativo": {
            "Presente": ["estoy", "estás", "está", "estamos", "estáis", "están"],
            "Pretérito Indefinido": ["estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"],
            "Pretérito Imperfecto": ["estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"],
            "Futuro Simple": ["estaré", "estarás", "estará", "estaremos", "estaréis", "estarán"],
            "Condicional Simple": ["estaría", "estarías", "estaría", "estaríamos", "estaríais", "estarían"],
            "Pretérito Perfecto Compuesto": ["he estado", "has estado", "ha estado", "hemos estado", "habéis estado", "han estado"],
            "Pretérito Pluscuamperfecto": ["había estado", "habías estado", "había estado", "habíamos estado", "habíais estado", "habían estado"],
            "Futuro Compuesto": ["habré estado", "habrás estado", "habrá estado", "habremos estado", "habréis estado", "habrán estado"],
            "Condicional Compuesto": ["habría estado", "habrías estado", "habría estado", "habríamos estado", "habríais estado", "habrían estado"],
        },
        "Subjuntivo": {
            "Presente": ["esté", "estés", "esté", "estemos", "estéis", "estén"],
            "Pretérito Imperfecto": ["estuviera", "estuvieras", "estuviera", "estuviéramos", "estuvierais", "estuvieran"],
            "Pretérito Perfecto Compuesto": ["haya estado", "hayas estado", "haya estado", "hayamos estado", "hayáis estado", "hayan estado"],
            "Pretérito Pluscuamperfecto": ["hubiera estado", "hubieras estado", "hubiera estado", "hubiéramos estado", "hubierais estado", "hubieran estado"],
            "Futuro Simple": ["estuviere", "estuvieres", "estuviere", "estuviéremos", "estuviereis", "estuvieren"],
        },
        "Imperativo": {
            "Afirmativo": ["-", "está", "esté", "estemos", "estad", "estén"],
            "Negativo": ["-", "no estés", "no esté", "no estemos", "no estéis", "no estén"],
        },
    },
    "haber": {
        "Indicativo": {
            "Presente": ["he", "has", "ha", "hemos", "habéis", "han"],
            "Pretérito Indefinido": ["hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron"],
            "Pretérito Imperfecto": ["había", "habías", "había", "habíamos", "habíais", "habían"],
            "Futuro Simple": ["habré", "habrás", "habrá", "habremos", "habréis", "habrán"],
            "Condicional Simple": ["habría", "habrías", "habría", "habríamos", "habríais", "habrían"],
            "Pretérito Perfecto Compuesto": ["he habido", "has habido", "ha habido", "hemos habido", "habéis habido", "han habido"],
            "Pretérito Pluscuamperfecto": ["había habido", "habías habido", "había habido", "habíamos habido", "habíais habido", "habían habido"],
            "Futuro Compuesto": ["habré habido", "habrás habido", "habrá habido", "habremos habido", "habréis habido", "habrán habido"],
            "Condicional Compuesto": ["habría habido", "habrías habido", "habría habido", "habríamos habido", "habríais habido", "habrían habido"],
        },
        "Subjuntivo": {
            "Presente": ["haya", "hayas", "haya", "hayamos", "hayáis", "hayan"],
            "Pretérito Imperfecto": ["hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"],
            "Pretérito Perfecto Compuesto": ["haya habido", "hayas habido", "haya habido", "hayamos habido", "hayáis habido", "hayan habido"],
            "Pretérito Pluscuamperfecto": ["hubiera habido", "hubieras habido", "hubiera habido", "hubiéramos habido", "hubierais habido", "hubieran habido"],
            "Futuro Simple": ["hubiere", "hubieres", "hubiere", "hubiéremos", "hubiereis", "hubieren"],
        },
        "Imperativo": {
            "Afirmativo": ["-", "he", "haya", "hayamos", "habed", "hayan"],
            "Negativo": ["-", "no hayas", "no haya", "no hayamos", "no hayáis", "no hayan"],
        },
    },
    "tener": {
        "Indicativo": {
            "Presente": ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"],
            "Pretérito Indefinido": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
            "Pretérito Imperfecto": ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
            "Futuro Simple": ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"],
            "Condicional Simple": ["tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"],
            "Pretérito Perfecto Compuesto": ["he tenido", "has tenido", "ha tenido", "hemos tenido", "habéis tenido", "han tenido"],
            "Pretérito Pluscuamperfecto": ["había tenido", "habías tenido", "había tenido", "habíamos tenido", "habíais tenido", "habían tenido"],
            "Futuro Compuesto": ["habré tenido", "habrás tenido", "habrá tenido", "habremos tenido", "habréis tenido", "habrán tenido"],
            "Condicional Compuesto": ["habría tenido", "habrías tenido", "habría tenido", "habríamos tenido", "habríais tenido", "habrían tenido"],
        },
        "Subjuntivo": {
            "Presente": ["tenga", "tengas", "tenga", "tengamos", "tengáis", "tengan"],
            "Pretérito Imperfecto": ["tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran"],
            "Pretérito Perfecto Compuesto": ["haya tenido", "hayas tenido", "haya tenido", "hayamos tenido", "hayáis tenido", "hayan tenido"],
            "Pretérito Pluscuamperfecto": ["hubiera tenido", "hubieras tenido", "hubiera tenido", "hubiéramos tenido", "hubierais tenido", "hubieran tenido"],
            "Futuro Simple": ["tuviere", "tuvieres", "tuviere", "tuviéremos", "tuviereis", "tuvieren"],
        },
        "Imperativo": {
            "Afirmativo": ["-", "ten", "tenga", "tengamos", "tened", "tengan"],
            "Negativo": ["-", "no tengas", "no tenga", "no tengamos", "no tengáis", "no tengan"],
        },
    },
    "hacer": {
        "Indicativo": {
            "Presente": ["hago", "haces", "hace", "hacemos", "hacéis", "hacen"],
            "Pretérito Indefinido": ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"],
            "Pretérito Imperfecto": ["hacía", "hacías", "hacía", "hacíamos", "hacíais", "hacían"],
            "Futuro Simple": ["haré", "harás", "hará", "haremos", "haréis", "harán"],
            "Condicional Simple": ["haría", "harías", "haría", "haríamos", "haríais", "harían"],
            "Pretérito Perfecto Compuesto": ["he hecho", "has hecho", "ha hecho", "hemos hecho", "habéis hecho", "han hecho"],
            "Pretérito Pluscuamperfecto": ["había hecho", "habías hecho", "había hecho", "habíamos hecho", "habíais hecho", "habían hecho"],
            "Futuro Compuesto": ["habré hecho", "habrás hecho", "habrá hecho", "habremos hecho", "habréis hecho", "habrán hecho"],
            "Condicional Compuesto": ["habría hecho", "habrías hecho", "habría hecho", "habríamos hecho", "habríais hecho", "habrían hecho"],
        },
        "Subjuntivo": {
            "Presente": ["haga", "hagas", "haga", "hagamos", "hagáis", "hagan"],
            "Pretérito Imperfecto": ["hiciera", "hicieras", "hiciera", "hiciéramos", "hicierais", "hicieran"],
            "Pretérito Perfecto Compuesto": ["haya hecho", "hayas hecho", "haya hecho", "hayamos hecho", "hayáis hecho", "hayan hecho"],
            "Pretérito Pluscuamperfecto": ["hubiera hecho", "hubieras hecho", "hubiera hecho", "hubiéramos hecho", "hubierais hecho", "hubieran hecho"],
            "Futuro Simple": ["hiciere", "hicieres", "hiciere", "hiciéremos", "hiciereis", "hicieren"],
        },
        "Imperativo": {
            "Afirmativo": ["-", "haz", "haga", "hagamos", "haced", "hagan"],
            "Negativo": ["-", "no hagas", "no haga", "no hagamos", "no hagáis", "no hagan"],
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
