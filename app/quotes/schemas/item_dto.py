from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    item_name: str
    description: str
    quantity: int
    unit_value: float
    created_at: datetime
    modified_on: datetime


class ItemCreate(ItemBase):
    quote_id: UUID


class ItemResponse(ItemBase):
    id: UUID
    quote_id: UUID

    class Config:
        orm_mode = True
