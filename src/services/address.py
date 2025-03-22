from sqlmodel.ext.asyncio.session import AsyncSession
from src.models.address import Address
from sqlalchemy.sql import select, desc, asc
from src.schemas.address import Address as AddressSchema, AddressUpdate as AddressUpdateSchema
from datetime import datetime
from fastapi import HTTPException

class AddressService:
    async def get_addresses(self, session: AsyncSession):
        statement = select(Address).order_by(desc(Address.created_at))

        result = await session.exec(statement)
        
        result = result.scalars().all()

        return result

    async def get_address(self, session: AsyncSession, address_id: int):
        statement = select(Address).where(Address.id == address_id)
        result = await session.exec(statement)
        
        return result.scalars().first() if result else None

    async def get_addresses_by_cust_id(self, session: AsyncSession, customer_id: int):
        statement = select(Address).where(Address.customer_id == customer_id).order_by(desc(Address.created_at))
        result = await session.exec(statement)
        
        return result.scalars().all()

    
    async def create_address(self, session: AsyncSession, address: AddressSchema):
        address_data = address.model_dump()
        
        new_address = Address(**address_data)
        
        session.add(new_address)
        await session.commit()
        
        return new_address

    async def update_address(self, session: AsyncSession, address_id: int, address: AddressUpdateSchema):
        address_update_data = await self.get_address(session, address_id)
        
        if not address_update_data:
            raise HTTPException(status_code=404, detail="Address not found")
        
        update_data = address.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if key == "updated_at" and value is None:
                setattr(address_update_data, key, datetime.now())
                
            setattr(address_update_data, key, value)
            
        await session.commit()
        
        return address_update_data

    async def delete_address(self, session: AsyncSession, address_id: int):
        address_delete_data = await self.get_address(session, address_id)
        
        if not address_delete_data:
            raise HTTPException(status_code=404, detail="Address not found")
        
        await session.delete(address_delete_data)
        await session.commit()