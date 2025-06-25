from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.db_models.user import User
from app.helpers.password_hash import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency to get the current authenticated user from the JWT token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Decode the JWT token
    payload = decode_access_token(token)
    if not payload:
        raise credentials_exception
    
    # Get user ID from token
    user_id = payload.get("sub")
    if not user_id:
        raise credentials_exception
    
    # Get user from database
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise credentials_exception
        
    return user
