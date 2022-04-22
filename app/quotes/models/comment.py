import uuid
from app.common.database import Base
from app.quotes.models import QT_TABLE_ARGS, QT_SCHEMA
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Comment(Base):
    __tablename__ = "comments"
    __table_args__ = (QT_TABLE_ARGS,)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    comment = Column(String, nullable=True)
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
