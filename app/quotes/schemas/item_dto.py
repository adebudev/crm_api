from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    item_name: str
    description: str
    quantity: int
    unit_value: int


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: UUID
    quantity: int
    unit_value: float
    description: str
    item_name: str
    quote_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class HttpResponse(BaseModel):
    status_code: str
    message: str
