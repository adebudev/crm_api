from uuid import UUID
from pydantic import BaseModel


class CommentBase(BaseModel):
    comment: str




class CommentResponse(CommentBase):
    id: UUID

    class Config:
        orm_mode = True
