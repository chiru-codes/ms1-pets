from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://mariela:@localhost:5432/pets_db"
    DEBUG: bool = False
    TESTING: bool = False
    ITEMS_PER_PAGE: int = 20
    LOG_LEVEL: str = "INFO"
    APP_ENV: str = "default"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
