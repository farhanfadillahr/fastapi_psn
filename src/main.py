from typing import Union, List

from fastapi import FastAPI

from .core.config import configs

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .core.config import configs
from .utils import singleton

from contextlib import asynccontextmanager
from src.core.databases import init_db
from src.routes import customers, address
from .middleware import register_middleware


    
    
@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=f"{configs.API}/openapi.json",
            version=configs.VERSION,
        )

        
        register_middleware(self.app)
        
        self.app.include_router(customers.customer_router, prefix="/customer", tags=["customer"])
        self.app.include_router(address.address_router, prefix="/address", tags=["address"])


print(configs.DATABASE_URI)
app_creator = AppCreator()
app = app_creator.app