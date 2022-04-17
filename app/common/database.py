from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.common.config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.database_hostname}:{settings.postgres_port}/{settings.postgres_db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


# Dependency
def get_db():
    print("get_db")
    db = SessionLocal()
    try:
        print("yield DB:", db)
        yield db
    finally:
        print("closing DB")
        db.close()
