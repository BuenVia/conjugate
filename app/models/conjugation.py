from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base import Base


class Conjugation(Base):
    __tablename__ = "conjugations"

    id = Column(Integer, primary_key=True, index=True)
    verb_id = Column(Integer, ForeignKey("verbs.id"), nullable=False, index=True)
    mood_id = Column(Integer, ForeignKey("moods.id"), nullable=False, index=True)
    tense_id = Column(Integer, ForeignKey("tenses.id"), nullable=False, index=True)
    person = Column(String, nullable=False)
    value = Column(String, nullable=False)
