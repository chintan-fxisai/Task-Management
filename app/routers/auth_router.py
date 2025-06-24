from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any

from app.database import get_db
from app.db_models.user import User
from app.api_schemas.user import UserRegister, UserRegisterResponse, UserLogin
from app.helpers.password_hash import hashed_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

@router.post("/register", response_model=UserRegisterResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserRegister, db: Session = Depends(get_db)):
    """
    Register a new user
    """
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_pw = hashed_password(user.password)
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_pw,
        role=user.role
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.post("/login")
async def login_user(
    login_data: UserLogin,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    User login endpoint, returns an access token for future requests
    """
    # Find user by email
    user = db.query(User).filter(User.email == login_data.email).first()
    
    # Verify user exists and password is correct
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    # Create access token
    access_token = create_access_token(
        data={"sub": str(user.id), "role": user.role}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role
        }
    }