from typing import List
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.schemas.address import Address as AddressSchema, AddressUpdate as AddressUpdateSchema
from src.services.address import AddressService
from src.core.databases import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

address_router = APIRouter()
address_service = AddressService()

# POST /address
@address_router.post("", response_model=AddressSchema,
                      status_code=status.HTTP_201_CREATED)
async def create_address(address: AddressSchema, session: AsyncSession = Depends(get_session)):
    new_address = await address_service.create_address(session, address)
    return new_address

# UPDATE /address/{address_id}   
@address_router.patch("/{address_id}", response_model=AddressSchema)
async def update_address(address_id: int, address: AddressUpdateSchema, session: AsyncSession = Depends(get_session)):
    updated_address = await address_service.update_address(session, address_id, address)
    
    if not updated_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    return updated_address

# DELETE /address/{address_id}
@address_router.delete("/{address_id}", response_model=None)
async def delete_address(address_id: int, session: AsyncSession = Depends(get_session)):
    deleted_address = await address_service.delete_address(session, address_id)
    return None

