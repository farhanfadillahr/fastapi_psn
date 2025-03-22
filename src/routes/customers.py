from typing import List
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.schemas.customers import Customer as CustomerSchema, CustomerUpdate as CustomerUpdateSchema
from src.services.customers import CustomersService
from src.core.databases import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

customer_router = APIRouter()
customer_service = CustomersService()

# GET /customers
@customer_router.get("", response_model=List[CustomerSchema])
async def get_customers(session: AsyncSession = Depends(get_session)):
    customers = await customer_service.get_customers(session)
    
    return customers

# GET Detail /customers/{customer_id}
@customer_router.get("/{customer_id}", response_model=CustomerSchema)
async def get_customer(customer_id: int, session: AsyncSession = Depends(get_session)):
    customer = await customer_service.get_customer(session, customer_id)
    
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
        
    return customer

# POST /customers
@customer_router.post("", response_model=CustomerSchema,
                      status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerSchema, session: AsyncSession = Depends(get_session)):
    new_customer = await customer_service.create_customer(session, customer)
    return new_customer

# UPDATE /customers/{customer_id}   
@customer_router.patch("/{customer_id}", response_model=CustomerSchema)
async def update_customer(customer_id: int, customer: CustomerUpdateSchema, session: AsyncSession = Depends(get_session)):
    updated_customer = await customer_service.update_customer(session, customer_id, customer)
    
    if not updated_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return updated_customer

# DELETE /customers/{customer_id}
@customer_router.delete("/{customer_id}", response_model=None)
async def delete_customer(customer_id: int, session: AsyncSession = Depends(get_session)):
    deleted_customer = await customer_service.delete_customer(session, customer_id)

    return None

