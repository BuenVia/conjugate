from pydantic import BaseModel


class VerbOut(BaseModel):
    id: int
    infinitive: str


class PersonConjugation(BaseModel):
    person: str
    value: str


class TenseOut(BaseModel):
    id: int
    name: str
    conjugations: list[PersonConjugation]


class MoodOut(BaseModel):
    id: int
    name: str
    tenses: list[TenseOut]


class VerbConjugationOut(BaseModel):
    verb: VerbOut
    moods: list[MoodOut]


class ErrorDetail(BaseModel):
    message: str


class ConjugationResponse(BaseModel):
    data: list[VerbConjugationOut]
    error: None = None


class ConjugationErrorResponse(BaseModel):
    data: None = None
    error: ErrorDetail
