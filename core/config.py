import secrets
import os
from dotenv import load_dotenv
load_dotenv()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "hng12-stage2"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "HNG12 DEVOPS x BACKEND (Stage 2)"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False
    EC2_IP: str = os.getenv("EC2_IP", "34.228.162.152")
    TICK_URL: str = f"http://{EC2_IP}.compute-1.amazonaws.com/api/v1/test/telex-webhook"
    SLACK_WEBHOOK_URL: str = os.getenv("SLACK_WEBHOOK_URL", "")
    APP_URL: str = f"http://{EC2_IP}.compute-1.amazonaws.com"


settings = Settings()
