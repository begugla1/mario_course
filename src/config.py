import os
from pathlib import Path


API_DIR = os.path.join(Path().resolve(), "api")

SMTP_USER = os.getenv("SMTP_USER", "null")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "null")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = os.getenv("SMTP_PORT", "465")

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")

print(API_DIR)