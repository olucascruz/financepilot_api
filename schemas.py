from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from datetime import date
from pydantic import Field
from typing import Optional

class MessageSchema(BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    email:str
    password: str

class UserPublic(BaseModel):
    id: int
    username: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    username: str | None = None

class CompanySchema(BaseModel):
    name: str
    business_area: str
    city: str
    state: str
    cnpj: str


class CompanyReadSchema(CompanySchema):
    id: int

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    create_at: date
    value: Decimal
    payament_method: str
    status: str
    cnpj: str = Field(..., min_length=14, max_length=18)

class OrderCreate(BaseModel):
    value: Decimal
    payament_method: str
    status: str
    cnpj: str = Field(..., min_length=14, max_length=18)

class OrderUpdate(BaseModel):
    create_at: date | None = None
    value: Decimal | None = None
    payament_method: str | None = None
    status: str | None = None
    cnpj: str | None = None

class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True



class TransactionBase(BaseModel):
    type: str
    category: str
    description: str
    value: Decimal
    status: str
    create_at: date

class TransactionCreate(TransactionBase):
    type: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Decimal] = None
    status: Optional[str] = None
    create_at: Optional[date] = None

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True

class TransactionUpdate(BaseModel):
    valor: Optional[float] = None
    descricao: Optional[str] = None
    tipo: Optional[str] = None

    class Config:
        from_attributes = True  # antes era orm_mode

class OrderUpdate(BaseModel):
    # Inclua os campos da Order que podem ser atualizados
    produto: Optional[str] = None
    quantidade: Optional[int] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True