from uuid import UUID
from psycopg2 import Date
from pydantic import BaseModel
from datetime import datetime


class ItemBase(BaseModel):
    quote_id: UUID
    quantity: int
    unit_value: int
    description: str
    item_name: str
    # date: datetime


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class HttpResponse(BaseModel):
    status_code: str
    message: str
