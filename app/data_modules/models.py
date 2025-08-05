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


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    business_area = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)


class Order(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    value = Column(String, nullable=False)
    payament_method = Column(String, nullable=False)
    status = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)