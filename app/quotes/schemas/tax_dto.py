from uuid import UUID
from typing import List
from pydantic import BaseModel
from datetime import datetime


class TaxBase(BaseModel):
    tax_name: str
    tax_value: float
    created_at: datetime
    modified_on: datetime


class TaxCreate(TaxBase):
    quote_id: UUID


class TaxResponse(TaxBase):
    id: UUID
    quote_id: UUID

    class Config:
        orm_mode = True
