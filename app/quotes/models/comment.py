import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import *
from sqlalchemy.orm import registry
from dataclasses import dataclass

mapper_registry = registry()

comments = Table(
    "comments",
    mapper_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("quote_id", UUID(as_uuid=True), ForeignKey("qt.quotes.id")),
    Column("comment", String, nullable=True),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
    Column("modified_on", DateTime, nullable=False, server_default=func.now()),
    schema="qt",
)


@dataclass
class Comment:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    id: uuid.UUID
    quote_id: uuid.UUID
    comment: str
    created_at: datetime
    modified_on: datetime


mapper_registry.map_imperatively(Comment, comments)
