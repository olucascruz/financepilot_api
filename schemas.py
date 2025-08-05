from pydantic import BaseModel
from datetime import datetime

class MessageSchema(BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    password: str

class UserPublic(BaseModel):
    id: int
    username: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenDataSchema(BaseModel):
    username: str | None = None