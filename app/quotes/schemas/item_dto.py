from uuid import UUID
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., alias="name")
    description: str = Field(..., alias="description")
    quantity: int = Field(..., alias="quantity")
    unit_value: float = Field(..., alias="unitValue")


class ItemResponse(ItemBase):
    id: UUID = Field(..., alias="id")
    quote_id: UUID = Field(..., alias="quoteId")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
