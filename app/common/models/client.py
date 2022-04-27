import uuid

from sqlalchemy import (
    Boolean,
    Column,
    String,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from app.common.models import MD_SCHEMA, MD_TABLE_ARGS
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from app.common.database import Base


class Client(Base):
    __tablename__ = "client"
    __table_args__ = (MD_TABLE_ARGS,)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    contact_name = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)
    contact_email = Column(String, nullable=True, unique=True)
    is_active = Column(Boolean, nullable=True, default=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey(MD_SCHEMA + "user.id", ondelete="CASCADE"))
    goverment_id = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))
    modified_on = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('now()'))
