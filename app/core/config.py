from pydantic import BaseSettings

class Settings(BaseSettings):
    Database_URL: str = "sqlite:///./ams.db"

settings = Settings()