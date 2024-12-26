from pydantic import BaseSettings, ValidationError

class Settings(BaseSettings):
    SCRAPER_URL: str
    REGEX_URL: str

    class Config:
        env_file = ".env"  # Specifies the environment file to load variables from

# Instantiate settings
try:
    settings = Settings()
except ValidationError as e:
    print(f"Configuration error: {e}")
    raise  # Re-raise the error to ensure the application doesn't run with incorrect configuration
