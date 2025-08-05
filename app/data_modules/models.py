from sqlalchemy import Column, Integer, ForeignKey, String, TIMESTAMP, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .settings import Base
import datetime


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

