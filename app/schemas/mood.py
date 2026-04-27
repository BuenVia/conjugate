from pydantic import BaseModel


class MoodOut(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class MoodListResponse(BaseModel):
    data: list[MoodOut]
    error: None = None
