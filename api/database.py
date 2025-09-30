import os 
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from .models import Base




db_url = os.getenv("DATABASE_URL")

if not db_url :
    raise RuntimeError("DATABASE_URL enviroment variable is not set.")
    
engine = create_engine(db_url, echo = False, pool_pre_ping=True)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit = False,autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()