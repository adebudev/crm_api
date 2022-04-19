import pytest
from app.api import app
from app.common.config import settings
from app.common.database import get_db
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.common.database import Base
from sqlalchemy import event
from sqlalchemy import DDL
from app.common.models import *
from app.quotes.models import *


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.postgres_test_user}:{settings.postgres_test_password}@{settings.database_test_hostname}:{settings.postgres_test_port}/{settings.postgres_test_db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    event.listen(Base.metadata, "before_create", DDL("CREATE SCHEMA IF NOT EXISTS md;"))
    event.listen(Base.metadata, "before_create", DDL("CREATE SCHEMA IF NOT EXISTS qt;"))
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_app(session):
    def test_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = test_get_db
    yield TestClient(app)
