from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    username: str = Field(..., min_length=5, max_length=35)
    email: EmailStr