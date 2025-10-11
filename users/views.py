from fastapi import APIRouter

from users.schemas import UserSchema
from users import crud

router = APIRouter(prefix='/users', tags=['Users'])

@router.post('/')
def add_user(user: UserSchema):
    return crud.create_user(new_user=user)