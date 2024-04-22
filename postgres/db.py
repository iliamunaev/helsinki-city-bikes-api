import os

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
async_engine = create_async_engine(DATABASE_URL, echo=True)

Base = declarative_base()


