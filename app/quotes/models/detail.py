import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, func, DateTime, String, Float, Integer
from sqlalchemy.orm import relationship

from app.quotes.models import QT_TABLE_ARGS
from app.common.database import Base


class Detail(Base):
    __tablename__ = "details"
    __table_args__ = QT_TABLE_ARGS

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    validity_time: Column(DateTime, nullable=False)
    deliver_time: Column(Integer, nullable=False)
    currency_type: Column(String, nullable=False)
    sub_total: Column(Float, nullable=False)
    total_price: Column(Float, nullable=False)
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    modified_on = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )

    quote_id = Column(UUID(as_uuid=True), ForeignKey("qt.quotes.id"))
