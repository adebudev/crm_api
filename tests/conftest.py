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

# TODO: fix test with new camelcase
@pytest.fixture
def session():
    event.listen(Base.metadata, "before_create", DDL("CREATE SCHEMA IF NOT EXISTS md;"))
    event.listen(Base.metadata, "before_create", DDL("CREATE SCHEMA IF NOT EXISTS qt;"))
    event.listen(Base.metadata, "before_create", DDL("CREATE SCHEMA IF NOT EXISTS iv;"))
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


@pytest.fixture
def test_user(test_app):
    user_data = {"email": "jhondoe@gmail.com", "password": "test"}
    res = test_app.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def test_client(test_app, test_user):
    client_data = {
        "name": "client_1",
        "address": "calle 10",
        "city": "Barranquilla",
        "country": "Colombia",
        "goverment_id": "12345679",
        "user_id": test_user["id"]
    }
    res = test_app.post("/client/", json=client_data)
    assert res.status_code == 201
    new_client = res.json()
    return new_client
