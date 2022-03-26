from app.common.database import Base
from app.common.models import MD_TABLE_ARGS
from sqlalchemy import Column, String, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
import hashlib

# TODO: continue defining user and make base model
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
    def password(self, pwd: str):
        """Password Setter"""
        self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def verify_password(self, password: str) -> bool:
        """
        Accept a password and hash the value while comparing the hashed
        value to the password hash contained in the database.
        """
        if self.password is None:
            return False
        pwd_e = password.encode()
        return hashlib.sha256(pwd_e).hexdigest().lower() == self.password
