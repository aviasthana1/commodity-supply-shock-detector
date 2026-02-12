from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CSSD_", extra="ignore")

    vol_z_threshold: float = 2.5
    news_hit_threshold: float = 0.6
