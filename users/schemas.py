from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    username: str
    name: str
    surname: str
    
class UserResponseModel(User):
    pass