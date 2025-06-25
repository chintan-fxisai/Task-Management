from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging
import traceback
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session
import os
import time
import threading
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, Any

from app.database import engine, get_db
from app.routers.auth_router import router as auth_router
from app.routers.protected_router import router as protected_router

# Global variable to store health status
health_status = {
    "status": "starting",
    "last_checked": None,
    "database": "disconnected",
    "uptime": 0,
    "start_time": time.time()
}

def check_health_continuously():
    """Background task to check health status every 10 seconds"""
    while True:
        try:
            # Check database connection
            db = next(get_db())
            db.execute(text("SELECT 1"))
            db_status = "connected"
            db.close()
            status = "healthy"
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Database health check failed: {error_msg}")
            db_status = f"error: {error_msg}"
            status = "unhealthy"
        
        # Get current time and uptime
        current_time = datetime.utcnow().isoformat()
        uptime = int(time.time() - health_status["start_time"])
        
        # Update health status
        health_status.update({
            "status": status,
            "last_checked": current_time,
            "database": db_status,
            "uptime": uptime
        })
        
        # Print status to terminal
        status_emoji = "✅" if status == "healthy" else "❌"
        print(f"\n{status_emoji} [Health Check - {current_time}]")
        print(f"Status: {status.upper()}")
        print(f"Database: {db_status}")
        print(f"Uptime: {uptime} seconds")
        print("-" * 50)
        
        # Wait for 10 seconds before next check
        time.sleep(10)

# Start the health check background task when the app starts
health_check_thread = threading.Thread(target=check_health_continuously, daemon=True)

# Load environment variables
load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "Task Management API"),
    description="API for managing tasks",
    version=os.getenv("PROJECT_VERSION", "0.1.0"),
    debug=True
)

# Logging configuration provides a way to log messages from the application to the terminal [INFO, DEBUG, WARNING, ERROR, CRITICAL]
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}\n{traceback.format_exc()}")
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal Server Error: {str(exc)}"},
    )

# Request validation error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Request validation error: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
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
    # Start the health check thread when the application starts
    health_check_thread.start()
    # Create database tables if they don't exist
    from app.db_models import Base
    Base.metadata.create_all(bind=engine)
    print("Database tables created")

@app.get("/")
async def root():
    return {"message": "Welcome to Task Management Application"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint that returns the current status of the application.
    The status is updated every 10 seconds by a background task.
    """
    if health_status["status"] != "healthy":
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "detail": "Service is not healthy"
            }
        )
    return health_status