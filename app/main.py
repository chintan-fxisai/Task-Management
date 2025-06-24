from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

from app.database import engine, get_db
from app.routers.auth_router import router as auth_router
from app.routers.protected_router import router as protected_router

# Load environment variables
load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "Task Management API"),
    description="API for managing tasks",
    version=os.getenv("PROJECT_VERSION", "0.1.0")
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(protected_router)

@app.on_event("startup")
async def startup():
    # Create database tables if they don't exist
    from app.db_models import Base
    Base.metadata.create_all(bind=engine)
    print("Database tables created")

@app.get("/")
async def root():
    return {"message": "Welcome to Task Management API"}

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Health check endpoint to verify database connection"""
    try:
        # Try to create a DB session
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )