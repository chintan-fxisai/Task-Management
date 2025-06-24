from pydantic import BaseModel
from pydantic.networks import EmailStr
class UserRegisterResponse(BaseModel):
    id:int
    full_name: str
    email: EmailStr

class config:
    orm_mode = True