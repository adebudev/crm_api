import uuid
from app.common.database import Base
from app.quotes.models import QT_TABLE_ARGS
from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Quote(Base):
    __tablename__ = "quotes"
    __table_args__ = (QT_TABLE_ARGS,)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quote_num = Column(Integer, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    client_id = Column(UUID(as_uuid=True), nullable=True)
    quote_status = Column(Boolean, nullable=False, default=True)
    exp_date = Column(TIMESTAMP(timezone=False), nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )
    modified_on = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )

    details = relationship("Detail")
    items = relationship("Item")
    taxes = relationship("Tax")
    comments = relationship("Comment")
