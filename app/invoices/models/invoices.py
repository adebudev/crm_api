import uuid
from app.common.database import Base
from app.invoices.models import IV_SCHEMA, IV_TABLE_ARGS
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Invoice(Base):
    __tablename__ = "invoices"
    __table_args__ = (IV_TABLE_ARGS,)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    invoice_num = Column(Integer, nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    detail = Column(String, nullable=False)
    total = Column(Numeric(precision=14, scale=2), nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )
    modified_on = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )
