import os

from pydantic_settings import BaseSettings, SettingsConfigDict

# BASE_DIR - loyihaning asosiy papkasi (bir papka yuqori database/ dan)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Settings(BaseSettings):
    DATABASE_URL:str
    bot_token: str
    model_config = SettingsConfigDict(
        # env_file="../.env",
        env_file=os.path.join(BASE_DIR, ".env"),
        case_sensitive=False,
    )


settings = Settings()
