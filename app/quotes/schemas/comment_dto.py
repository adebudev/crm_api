from uuid import UUID
from pydantic import BaseModel, Field


class CommentBase(BaseModel):
    comment: str = Field(..., alias="comment")


class CommentResponse(CommentBase):
    id: UUID = Field(..., alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
