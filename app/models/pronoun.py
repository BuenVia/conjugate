from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Pronoun(Base):
    __tablename__ = "pronouns"

    id = Column(Integer, primary_key=True, index=True)
    pronoun = Column(String, unique=True, nullable=False)
