import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import relationship

from app.quotes.models import QT_TABLE_ARGS

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    __table_args__ = QT_TABLE_ARGS

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quantity = Column(String, nullable=False)
    unit_value = Column(String, nullable=False)
    description = Column(String, nullable=False)
    item_name = Column(String, nullable=False)
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    modified_on = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )

    quote_id = Column(UUID(as_uuid=True), ForeignKey("qt.quotes.id"))
