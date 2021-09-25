import logging

from pydantic import BaseSettings

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///../database.sqlite3'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
