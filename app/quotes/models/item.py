import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import *
from sqlalchemy.orm import registry
from dataclasses import dataclass

mapper_registry = registry()

items = Table(
    "items",
    mapper_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("quote_id", UUID(as_uuid=True), ForeignKey("quotes.id")),
    Column("item_name", String, nullable=True),
    Column("description", String, nullable=True),
    Column("quantity", Integer, nullable=True),
    Column("unit_value", Float, nullable=True),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
    Column("modified_on", DateTime, nullable=False, server_default=func.now()),
    schema="qt",
)


@dataclass
class Item:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    id: uuid.UUID
    quote_id: uuid.UUID
    item_name: str
    description: str
    quantity: int
    unit_value: float
    created_at: datetime
    modified_on: datetime


mapper_registry.map_imperatively(Item, items)
