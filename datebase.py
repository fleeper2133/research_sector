from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL = "postgresql://postgres:admin@localhost:5432/fastapi"

engine = create_engine(SQLALCHEMY_URL, echo=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
