from uuid import UUID
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    quantity: int
    unit_value: float



class ItemResponse(ItemBase):
    id: UUID
    quote_id: UUID

    class Config:
        orm_mode = True
