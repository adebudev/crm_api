import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, func, DateTime, String
from sqlalchemy.orm import relationship
from app.quotes.models import QT_TABLE_ARGS, QT_SCHEMA
from app.common.database import Base


class Comment(Base):
    __tablename__ = "comments"
    __table_args__ = QT_TABLE_ARGS

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    comment = Column(String, nullable=False)
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    modified_on = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )

    quote_id = Column(UUID(as_uuid=True), ForeignKey(QT_SCHEMA + "quotes.id"))
