import dotenv
from dotenv import load_dotenv
from fastapi import Path
from pydantic.v1 import BaseSettings

load_dotenv()


class PostgresSettings(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DATABASE: str

    @property
    def url(self) -> str:
        return f'postgres://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'

    class Config:
        case_sensitive = False
        env_prefix = "PG_"


class AppSettings(BaseSettings):
    PORT: int = 8080
    IS_DEBUG: bool = True

    TITLE: str = 'Helsinki City Bikes API'
    VERSION: str = '0.1.0'

    class Config:
        case_sensitive = False
