from pydantic import BaseModel


class TenseOut(BaseModel):
    id: int
    name: str
    mood_id: int
    mood_name: str

    model_config = {"from_attributes": True}


class TenseListResponse(BaseModel):
    data: list[TenseOut]
    error: None = None
