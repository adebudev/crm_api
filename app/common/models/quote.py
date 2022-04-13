import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship

from app.common.models import MD_TABLE_ARGS
from app.common.database import Base

class Quote(Base):
    __tablename__ = "quotes"
    __table_args__ = (MD_TABLE_ARGS)
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quote_num = Column(Integer, nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("md.users.id"), nullable=False)
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    modified_on = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )

    user = relationship("User", back_populates="quotes")
    items = relationship("Item", cascade="all, delete")
