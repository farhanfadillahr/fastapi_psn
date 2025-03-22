from sqlmodel.ext.asyncio.session import AsyncSession
from src.models.customers import Customer
from sqlalchemy.sql import select, desc, asc
from src.schemas.customers import Customer as CustomerSchema, CustomerUpdate as CustomerUpdateSchema
from datetime import datetime
from fastapi import HTTPException
from .address import AddressService
from src.schemas.address import Address as AddressSchema
from typing import List

address_service = AddressService()

class CustomersService:
    async def get_customers(self, session: AsyncSession):
        statement = select(Customer).order_by(asc(Customer.name), asc(Customer.id))

        result = await session.exec(statement)
        
        result = result.scalars().all()

        return result

    async def get_customer(self, session: AsyncSession, customer_id: int):
        # Query pertama: Ambil data customer
        customer_stmt = select(Customer).where(Customer.id == customer_id)
        customer_result = await session.execute(customer_stmt)
        customer = customer_result.scalars().first()

        if not customer:
            return None

        # Query kedua: Ambil semua alamat terkait dengan customer_id
        addresses = await address_service.get_addresses_by_cust_id(session, customer_id)
        address_list = [AddressSchema.model_dump(addr) for addr in addresses]

        # Konversi ke Pydantic schema
        customer_data = CustomerSchema(
            id=customer.id,
            title=customer.title,
            name=customer.name,
            gender=customer.gender,
            phone_number=customer.phone_number,
            image=customer.image,
            email=customer.email,
            address=address_list,
            created_at=customer.created_at,
            updated_at=customer.updated_at
        )

        return customer_data

    async def create_customer(self, session: AsyncSession, customer: CustomerSchema):
        customer_data = customer.model_dump()
        
        new_customer = Customer(**customer_data)
        
        session.add(new_customer)
        await session.commit()
        
        return new_customer

    async def update_customer(self, session: AsyncSession, customer_id: int, customer: CustomerUpdateSchema):
        customer_update_data = await self.get_customer(session, customer_id)
        
        if not customer_update_data:
            raise HTTPException(status_code=404, detail="Customer not found")
        
        update_data = customer.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if key == "updated_at" and value is None:
                setattr(customer_update_data, key, datetime.now())
                
            setattr(customer_update_data, key, value)
            
        await session.commit()
        
        return customer_update_data

    async def delete_customer(self, session: AsyncSession, customer_id: int):
        customer_delete_data = await self.get_customer(session, customer_id)
        
        if not customer_delete_data:
            raise HTTPException(status_code=404, detail="Customer not found")
        
        await session.delete(customer_delete_data)
        await session.commit()
        
        