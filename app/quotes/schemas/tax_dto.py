from uuid import UUID
from typing import List
from pydantic import BaseModel
from datetime import datetime


class TaxBase(BaseModel):
    tax_name: str
    tax_percentage: float


class TaxCreate(TaxBase):
    pass


class TaxResponse(TaxBase):
    id: UUID
    iva: float
    diam_tax: float
    contingency: float
    other: float
    detail_id: UUID

    class Config:
        orm_mode = True
