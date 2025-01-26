from pydantic import Field
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    HOST: str = Field(alias="POSTGRES_HOST")
    PORT: str = Field(alias="POSTGRES_PORT")
    NAME: str = Field(alias="POSTGRES_DB")
    USER: str = Field(alias="POSTGRES_USER")
    PASS: str = Field(alias="POSTGRES_PASSWORD")


class Settings(BaseSettings):
    db: DBSettings = DBSettings()


settings = Settings()
