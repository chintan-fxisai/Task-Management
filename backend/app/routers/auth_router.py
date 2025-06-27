import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any
import traceback

from app.database import get_db
from app.db_models.user import User
from app.api_schemas.user import UserRegister, UserRegisterResponse, UserLogin
from app.helpers.password_hash import hashed_password, verify_password, create_access_token

logger = logging.getLogger(__name__)

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
    try:
        logger.info(f"Login attempt for email: {login_data.email}")
        
        # Find user by email
        user = db.query(User).filter(User.email == login_data.email).first()
        
        if not user:
            logger.warning(f"Login failed: User with email {login_data.email} not found")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Verify password
        if not verify_password(login_data.password, user.password):
            logger.warning(f"Login failed: Invalid password for user {login_data.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Check if user is active
        if not user.is_active:
            logger.warning(f"Login failed: Inactive user {login_data.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )
        
        # Create access token
        try:
            access_token = create_access_token(
                data={"sub": str(user.id), "role": user.role}
            )
            
            response_data = {
                "access_token": access_token,
                "token_type": "bearer",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "full_name": user.full_name,
                    "role": user.role
                }
            }
            
            logger.info(f"Login successful for user {user.email}")
            return response_data
            
        except Exception as token_error:
            logger.error(f"Token creation failed: {str(token_error)}\n{traceback.format_exc()}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error generating access token"
            )
            
    except HTTPException as http_exc:
        # Re-raise HTTP exceptions
        raise http_exc
        
    except Exception as e:
        logger.error(f"Unexpected error during login: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred during login"
        )