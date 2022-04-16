import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, Integer, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship

from app.quotes.models import QT_TABLE_ARGS, QT_SCHEMA
from app.common.database import Base


class Quote(Base):
    __tablename__ = "quotes"
    __table_args__ = QT_TABLE_ARGS

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        return f"<Quote(id={self.id})>"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quote_num = Column(Integer, nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    customer_id: Column(UUID(as_uuid=True), nullable=True)
    quote_status: Column(Boolean, nullable=True)
    exp_date: Column(DateTime, nullable=True)
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    modified_on = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
