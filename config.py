import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ORIGINS = os.getenv("ORIGIN")
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()

print(f"Loaded settings: SECRET_KEY={settings.SECRET_KEY}, ORIGINS={settings.ORIGINS}, DATABASE_URL={settings.DATABASE_URL}")