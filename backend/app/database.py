import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

__all__ = ["Base", "SessionLocal", "get_db", "engine"]

# Load environment variables
load_dotenv()

# Get database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Fallback to SQLite if DATABASE_URL is not set
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./task_management.db"

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    # Only needed for SQLite
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for models
Base = declarative_base()

def get_db():
    """Dependency to get DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
