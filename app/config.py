"""
Application configuration using Pydantic Settings.
All configuration is loaded from environment variables.
"""
from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    openai_api_key: str
    llm_provider: Literal["openai", "claude"] = "openai"
    model_name: str = "gpt-4-turbo-preview"
    max_tokens: int = 2000
    temperature: float = 0.7
    
    database_url: str
    redis_url: str
    
    debug: bool = False
    log_level: str = "INFO"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    session_ttl: int = 7200
    max_retries: int = 3
    retry_delay: int = 1
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()