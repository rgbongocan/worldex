from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    project_name: str
    version: str
    database_url: str
    database_echo_query: bool = False