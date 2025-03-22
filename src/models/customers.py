from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from datetime import datetime
import sqlalchemy.dialects.mysql as my
from typing import Optional, List
# from .address import Address

class Customer(SQLModel, table=True):
    __tablename__ = "customers"

    id : int = Field(
        sa_column=Column(Integer, primary_key=True)
    )
    title : str
    name : str
    gender : str
    phone_number : str
    image : str
    email : str
    created_at : datetime = Field(
        sa_column=Column(my.TIMESTAMP , default=datetime.now, nullable=False)
    )
    updated_at : datetime = Field(
        sa_column=Column(my.TIMESTAMP , default=datetime.now, onupdate=datetime.now, nullable=False)
    )
    
    
    def __repr__(self):
        return f"<Customer {self.name}>"

    addresses: List["Address"] = Relationship(back_populates="customer")