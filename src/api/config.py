import os


SMTP_USER = os.getenv("SMTP_USER", "null")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "null")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = os.getenv("SMTP_PORT", "465")
