from uuid import UUID
from pydantic import BaseModel


class TaxBase(BaseModel):
    tax_name: str
    tax_value: float



class TaxResponse(TaxBase):
    id: UUID
    quote_id: UUID

    class Config:
        orm_mode = True
