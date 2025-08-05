from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..data_modules.database import get_session
from ..data_modules.models import User

from schemas import UserPublic, UserSchema
from security import get_current_user, get_password_hash


router = APIRouter(prefix='/users', tags=['users'])
DbSession = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]

@router.post("/register", status_code=201, response_model=UserPublic)
async def register( user: UserSchema,
    db:DbSession
    ):

    hashed_password = get_password_hash(user.password)

    db_user = User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user