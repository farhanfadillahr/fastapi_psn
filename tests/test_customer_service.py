import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from unittest.mock import AsyncMock
from src.services.customers import CustomersService
from src.services.address import AddressService
from src.schemas.customers import Customer as CustomerSchema
from src.schemas.address import Address as AddressSchema
from fastapi import HTTPException

@pytest.mark.asyncio
async def test_get_customer_success():
    session = AsyncMock(AsyncSession)

    # Mock Customer
    mock_customer = CustomerSchema(
        id=1,
        title="Mr",
        name="Adrien Philippe",
        gender="M",
        phone_number="085222334445",
        image="https://img.freepik.com/premium-vector/man-avatar-profile-round-icon_24640-14044.jpg",
        email="adrien.philippe@gmail.com",
        created_at="2020-08-01 10:56:31",
        updated_at="2020-08-08 09:30:23"
    )

    # Mock Address
    mock_addresses = AddressSchema(
            id=1,
            customer_id=1,
            address="Kawasan Karyadeka Pancamurni Blok A Kav. 3",
            district="Cikarang Selatan",
            city="Bekasi",
            province="Jawa Barat",
            postal_code=17530,
            created_at="2020-08-01 10:56:31",
            updated_at="2020-08-08 09:30:23"
        )
    
    # Service Call
    service_cust = CustomersService()
    customer = await service_cust.create_customer(session, mock_customer)
    service_addr = AddressService()
    addresses = await service_addr.create_address(session, mock_addresses)

    # Mock Query Execution
    session.execute.side_effect = [
        AsyncMock(return_value=AsyncMock(scalars=AsyncMock(first=mock_customer))),  # Customer Query
        AsyncMock(return_value=AsyncMock(scalars=AsyncMock(all=mock_addresses)))   # Address Query
    ]

    
    # addresses = await service_addr.get_addresses_by_cust_id(session, mock_addresses)

    # Assertions
    assert customer is not None
    assert customer.id == 1
    assert customer.name == "Adrien Philippe"
    assert addresses is not None
    assert addresses.id == 1
    assert addresses.customer_id == 1