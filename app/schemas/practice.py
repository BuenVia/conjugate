from pydantic import BaseModel


class PracticeItem(BaseModel):
    id: int
    infinitive: str
    mood: str
    tense: str
    pronoun: str
    conjugation: str


class ErrorDetail(BaseModel):
    message: str


class PracticeResponse(BaseModel):
    data: list[PracticeItem]
    error: None = None


class PracticeErrorResponse(BaseModel):
    data: None = None
    error: ErrorDetail
