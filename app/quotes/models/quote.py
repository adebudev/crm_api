from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

# from sqlalchemy import Boolean, Column, Integer, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.quotes.models import QT_TABLE_ARGS, QT_SCHEMA

from sqlalchemy import *
from sqlalchemy.orm import registry
from dataclasses import dataclass

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


mapper_registry.map_imperatively(Quote, quotes)

# __tablename__ = "quotes"
# __table_args__ = (QT_TABLE_ARGS,)

# def __init__(self, **kwargs):
#     self.__dict__.update(kwargs)

# def __repr__(self) -> str:
#     return f"<Quote(id={self.id})>"

# id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
# quote_num = Column(Integer, nullable=False, unique=True)
# user_id = Column(UUID(as_uuid=True), nullable=True)
# customer_id: Column(UUID(as_uuid=True), nullable=True)
# quote_status: Column(Boolean, nullable=True)
# exp_date: Column(DateTime, nullable=True)
# created_at = Column(
#     DateTime, nullable=False, server_default=func.now(), default=func.now()
# )
# modified_on = Column(
#     DateTime, nullable=False, server_default=func.now(), default=func.now()
# )
