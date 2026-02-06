"""
Project Chimera: Application configuration
"""
import os
from typing import List

# CORS
CORS_ORIGINS: List[str] = os.getenv("CORS_ORIGINS", "*").split(",") if os.getenv("CORS_ORIGINS") else ["*"]

# Debug
DEBUG: bool = os.getenv("ENVIRONMENT", "development").lower() != "production"

# Database
POSTGRES_URL: str = os.getenv("POSTGRES_URL", "postgresql://localhost:5432/chimera")
REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# API Keys (loaded from env)
WEAVIATE_URL: str = os.getenv("WEAVIATE_URL", "")
WEAVIATE_API_KEY: str = os.getenv("WEAVIATE_API_KEY", "")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "") or os.getenv("GOOGLE_API_KEY", "")
NEWSDATA_API_KEY: str = os.getenv("NEWSDATA_API_KEY", "")


class Settings:
    CORS_ORIGINS: List[str] = CORS_ORIGINS
    DEBUG: bool = DEBUG
    POSTGRES_URL: str = POSTGRES_URL
    REDIS_URL: str = REDIS_URL
    WEAVIATE_URL: str = WEAVIATE_URL
    WEAVIATE_API_KEY: str = WEAVIATE_API_KEY
    GEMINI_API_KEY: str = GEMINI_API_KEY
    NEWSDATA_API_KEY: str = NEWSDATA_API_KEY


settings = Settings()
