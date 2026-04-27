from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Tense(Base):
    __tablename__ = "tenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mood_id = Column(Integer, ForeignKey("moods.id"), nullable=False, index=True)

    mood = relationship("Mood", back_populates="tenses")
