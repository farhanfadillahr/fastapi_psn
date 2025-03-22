from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from datetime import datetime
import sqlalchemy.dialects.mysql as my
from typing import Optional, List
# from .customers import Customer

class Address(SQLModel, table=True):
    __tablename__ = "addresses"
    
    id : int = Field(
        sa_column=Column(Integer, primary_key=True)
    )
    customer_id: int = Field(foreign_key="customers.id", nullable=True)
    address: str
    district: str
    city: str
    province: str
    postal_code: int
    created_at: datetime = Field(
        sa_column=Column(my.TIMESTAMP , default=datetime.now, nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(my.TIMESTAMP, default=datetime.now, onupdate=datetime.now, nullable=False)
    )

    customer: Optional["Customer"] = Relationship(back_populates="addresses")