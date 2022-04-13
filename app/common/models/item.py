import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, String, func, DateTime
from sqlalchemy.orm import relationship

from app.common.models import MD_TABLE_ARGS
from app.common.database import Base

class Item(Base):
    __tablename__ = "items"
    __table_args__ = (MD_TABLE_ARGS)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quantity = Column(String, index=True)
    unit_value = Column(String, index=True)
    description = Column(String, index=True)
    item_name = Column(String, index=True)
    quote_id = Column(UUID(as_uuid=True), ForeignKey("md.quotes.id"), nullable=False)
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    modified_on = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    quote = relationship("Quote", back_populates="items")