from pydantic import BaseModel


class PronounOut(BaseModel):
    id: int
    pronoun: str

    model_config = {"from_attributes": True}


class PronounListResponse(BaseModel):
    data: list[PronounOut]
    error: None = None
