from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..data_modules.database import get_session
from ..data_modules.models import Order, User
from schemas import (
    OrderCreate,
    OrderResponse,
)

from security import get_current_user

router = APIRouter(prefix="/order", tags=["order"])
DbSession = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_session)):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: DbSession):
    return db.query(Order).filter(Order.id == order_id).first()


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: DbSession):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: DbSession):
    return db.query(Order).filter(Order.id == order_id).first()
