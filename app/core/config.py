from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "OpenEmbed API")
    API_VERSION = os.getenv("API_VERSION", "v1")
    MODEL_NAME = os.getenv("MODEL_NAME", "BAAI/bge-small-en-v1.5")

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"


settings = Settings()