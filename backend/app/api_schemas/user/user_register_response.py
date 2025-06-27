from uuid import UUID
from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserRegisterResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr

    class Config:
        orm_mode = True