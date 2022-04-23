from uuid import UUID
from pydantic import BaseModel, Field


class TaxBase(BaseModel):
    tax_name: str = Field(..., alias="taxName")
    tax_value: float = Field(..., alias="taxValue")


class TaxResponse(TaxBase):
    id: UUID = Field(..., alias="id")
    quote_id: UUID = Field(..., alias="quoteId")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
