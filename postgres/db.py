from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

import asyncio

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/helsinkibikes"
async_engine = create_async_engine(DATABASE_URL, echo=True)

Base = declarative_base()


