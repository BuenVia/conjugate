from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Verb(Base):
    __tablename__ = "verbs"

    id = Column(Integer, primary_key=True, index=True)
    infinitive = Column(String, unique=True, nullable=False, index=True)
