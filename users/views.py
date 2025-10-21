from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud

from .schemas import UserResponseModel

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/', response_model=list[UserResponseModel])
async def get_users(session: AsyncSession = Depends(db_helper.get_scoped_session)):
    return await crud.get_users(session=session)

@router.get('/{user_id}', response_model=UserResponseModel)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(db_helper.get_scoped_session)):
    user = await crud.get_user_by_id(session=session, user_id=user_id)
    if user is not None:
        return user
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='User not found :('
    )