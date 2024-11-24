import os
from typing import Optional
from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    """
    To define all environment variables
    """
    QDRANT_API_KEY:str = os.getenv("QDRANT_API_KEY", "")

settings = Settings()