from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FOLLAR Agent API"
    app_version: str = "1.0.0"
    debug: bool = False
    wandb_project: str = "follar-agent-v1"
    database_url: str = "sqlite:///./follar_agent.db"
    health_check_interval_ms: int = 1000000 # 1.000.000 ms = ~16.6 minutos

    class Config:
        env_file = ".env"

settings = Settings()