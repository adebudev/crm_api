import uuid
from app.common.database import Base
from app.quotes.models import QT_TABLE_ARGS, QT_SCHEMA
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Detail(Base):
    __tablename__ = "details"
    __table_args__ = (QT_TABLE_ARGS,)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    valid_time = Column(Integer, nullable=True)
    deliver_time = Column(TIMESTAMP(timezone=False), nullable=True)
    # TODO: change to enum
    currency_type = Column(String, nullable=True)
    payment_terms = Column(String, nullable=True)
    sub_total = Column(Numeric(precision=14, scale=2), nullable=True)
    total = Column(Numeric(precision=14, scale=2), nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )
    modified_on = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )

    # Foreign key
    quote_id = Column(
        UUID(as_uuid=True), ForeignKey(QT_SCHEMA + "quotes.id", ondelete="CASCADE")
    )
