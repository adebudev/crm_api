import uuid
from app.common.database import Base
from app.quotes.models import QT_TABLE_ARGS, QT_SCHEMA
from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Item(Base):
    __tablename__ = "items"
    __table_args__ = (QT_TABLE_ARGS,)


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item_name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    quantity = Column(Integer, nullable=True)
    unit_value = Column(Float, nullable=True)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))
    modified_on = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))


    # Foreign keys
    quote_id = Column(UUID(as_uuid=True), ForeignKey(QT_SCHEMA + "quotes.id", ondelete="CASCADE"))

