from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..data_modules.database import get_session
from ..data_modules.models import Transactions, User
from schemas import (
    TransactionCreate,
    TransactionResponse,
)

from security import get_current_user

router = APIRouter(prefix="/transaction", tags=["transaction"])
DbSession = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post("/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: DbSession):
    db_transaction = Transactions(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: DbSession):
    return db.query(Transactions).filter(Transactions.id == transaction_id).first()
