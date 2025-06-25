from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: Optional[str] = "employee"

class config:
    orm_mode = True