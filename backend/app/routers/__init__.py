"""
API routers package.
"""

from app.routers.auth_router import router as auth_router
from app.routers.protected_router import router as protected_router

__all__ = ["auth_router", "protected_router"]
