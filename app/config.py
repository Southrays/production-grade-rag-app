from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    #LLM Configuration
    openai_api_key: str
    primary_model: str = "gpt-4o-mini"
    fallback_model: str = "gpt-4o-mini"  #Youc can change fallback model

    #LangSmith
    langchain_tracing_v2: bool = True
    langchain_api_key: str = ""
    langchain_project: str = "production-api"

    #Application
    app_env: str = "development"
    log_level: str = "INFO"
    rate_limit: str = "20/minute"
    cache_ttl_seconds: int = 300
    max_retries: int = 3

    model_config = {"env_file": ".env", "extra": "ignore"}

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"



@lru_cache
def get_settings() -> Settings:
    """Cached Settings instance - loaded once, reused everywhere."""
    return Settings()  # type: ignore[call-arg]
