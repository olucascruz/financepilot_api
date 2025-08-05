from pydantic import BaseModel
from datetime import datetime

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
        orm_mode = True