import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import *
from sqlalchemy.orm import registry
from dataclasses import dataclass

mapper_registry = registry()

details = Table(
    "details",
    mapper_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("quote_id", UUID(as_uuid=True), ForeignKey("qt.quotes.id")),
    Column("valid_time", Integer, nullable=True),
    Column("deliver_time", DateTime, nullable=True),
    Column("currency_type", String, nullable=True),
    Column("payment_terms", String, nullable=True),
    Column("sub_total", Float, nullable=True),
    Column("total", Float, nullable=True),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
    Column("modified_on", DateTime, nullable=False, server_default=func.now()),
    schema="qt",
)


@dataclass
class Detail:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    id: uuid.UUID
    quote_id: uuid.UUID
    valid_time: int
    deliver_time: datetime
    currency_type: str
    payment_terms: str
    sub_total: float
    total: float
    created_at: datetime
    modified_on: datetime


mapper_registry.map_imperatively(Detail, details)
