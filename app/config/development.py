from .default import Settings as DefaultSettings


class DevelopmentSettings(DefaultSettings):
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"

    DATABASE_URL: str = "postgresql+psycopg2://mariela:@localhost:5432/pets_dev"
