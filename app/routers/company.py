from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..data_modules.database import get_session
from ..data_modules.models import User

from schemas import CompanySchema, CompanyReadSchema
from security import get_current_user, get_password_hash
from ..data_modules.models import Company

router = APIRouter(prefix='/company', tags=['company'])
DbSession = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]

@router.post("/", response_model=CompanyReadSchema)
def create_company(company: CompanySchema, db: DbSession):
    db_company = Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
