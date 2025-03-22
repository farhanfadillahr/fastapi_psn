from pydantic import BaseModel, field_serializer
from datetime import datetime
from typing import List, Optional

class Address(BaseModel):
    id: Optional[int] = None
    customer_id: Optional[int] = None
    address: str
    district: str
    city: str
    province: str
    postal_code: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    
    @field_serializer("created_at", "updated_at")
    def serialize_datetime(self, dt: Optional[datetime], _info):
        if dt is None:
            return None  # Return None jika tidak ada nilai
        return dt.strftime("%Y-%m-%d %H:%M:%S")
            

class AddressUpdate(BaseModel):
    customers_id: Optional[int] = None
    address: Optional[str] = None
    district: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    updated_at: Optional[datetime] = None
    

    
    