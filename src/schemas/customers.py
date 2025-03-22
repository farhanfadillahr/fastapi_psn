from pydantic import BaseModel, field_serializer
from datetime import datetime
from typing import List, Optional
from .address import Address

class Customer(BaseModel):
    id: Optional[int] = None
    title: str
    name: str
    gender: str
    phone_number: str
    image: str
    email: str
    address: Optional[List[Address]] = []
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @field_serializer("created_at", "updated_at")
    def serialize_datetime(self, dt: Optional[datetime], _info):
        if dt is None:
            return None  # Return None jika tidak ada nilai
        return dt.strftime("%Y-%m-%d %H:%M:%S")
            
class CustomerUpdate(BaseModel):
    title: Optional[str] = None
    name: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    image: Optional[str] = None
    email: Optional[str] = None
    updated_at: Optional[datetime] = None
    

    
    