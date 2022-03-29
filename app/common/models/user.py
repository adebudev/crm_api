from app.common.database import Base
from app.common.models import MD_TABLE_ARGS
from sqlalchemy import Column, String, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "user"
    __table_args__ = (MD_TABLE_ARGS,)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False, unique=True)
    _password = Column(String, nullable=False)
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )
    modified_on = Column(
        DateTime, nullable=False, server_default=func.now(), default=func.now()
    )

    @property
    def password(self) -> str:
        """Password Getter"""
        return self._password

    @password.setter
    def password(self, password: str):
        """Password Setter"""
        self._password = pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Accept a password and hash the value while comparing the hashed
        value to the password hash contained in the database.
        """
        if self.password is None:
            return False
        return pwd_context.verify(plain_password, hashed_password)
