from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.db_models.user import User

router = APIRouter(
    prefix="/api",
    tags=["protected"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Get current user information
    """
    return {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "role": current_user.role,
        "is_active": current_user.is_active
    }
