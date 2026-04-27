from pydantic import BaseModel


class VerbOut(BaseModel):
    id: int
    infinitive: str

    model_config = {"from_attributes": True}


class VerbListResponse(BaseModel):
    data: list[VerbOut]
    error: None = None
