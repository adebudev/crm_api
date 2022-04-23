from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class DetailBase(BaseModel):
    valid_time: int = Field(..., alias="validTime")
    deliver_time: datetime = Field(..., alias="deliverTime")
    currency_type: Optional[str] = Field(None, alias="currencyType")
    payment_terms: str = Field(..., alias="paymentTerms")
    sub_total: float = Field(..., alias="subTotal")
    total: float = Field(..., alias="total")


class DetailResponse(DetailBase):
    id: UUID
    created_at: datetime = Field(..., alias="createdAt")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
