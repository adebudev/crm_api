from dataclasses import field
from typing import List
import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import *
from sqlalchemy.orm import registry, relationship
from dataclasses import dataclass

from app.quotes.models.detail import Detail

mapper_registry = registry()


quotes = Table(
    "quotes",
    mapper_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("quote_num", String, nullable=False, unique=True),
    Column("user_id", UUID(as_uuid=True), nullable=True),
    Column("customer_id", UUID(as_uuid=True), nullable=True),
    Column("quote_status", Boolean, nullable=True),
    Column("exp_date", DateTime, nullable=True),
    Column(
        "created_at",
        DateTime,
        nullable=False,
        server_default=func.now(),
        default=func.now(),
    ),
    Column(
        "modified_on",
        DateTime,
        nullable=False,
        server_default=func.now(),
        default=func.now(),
    ),
    schema="qt",
)


@dataclass
class Quote:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    id: uuid.UUID
    quote_num: str
    user_id: uuid.UUID
    customer_id: uuid.UUID
    quote_status: bool
    exp_date: datetime
    created_at: datetime
    modified_on: datetime
    # details: List[Detail] = field(default_factory=list)


mapper_registry.map_imperatively(
    Quote,
    quotes,
)
