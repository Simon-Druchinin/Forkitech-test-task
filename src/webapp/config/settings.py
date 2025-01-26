from pydantic import BaseModel, Field


class DBSettings(BaseModel):
    HOST: str = Field(alias="POSTGRES_HOST")
    PORT: str = Field(alias="POSTGRES_PORT")
    NAME: str = Field(alias="POSTGRES_DB")
    USER: str = Field(alias="POSTGRES_USER")
    PASS: str = Field(alias="POSTGRES_PASSWORD")


class Settings(BaseModel):
    db: DBSettings = DBSettings()


settings = Settings()
