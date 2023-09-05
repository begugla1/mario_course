import os
from pathlib import Path


API_DIR = os.path.join(Path().resolve(), "api")

DB_HOST = os.environ.get("DB_HOST", "database")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")

# TODO move test settings to tests dir
TEST_DB_HOST = os.environ.get("TEST_DB_HOST", "test_database")
TEST_DB_PORT = os.environ.get("TEST_DB_PORT", "6432")
TEST_DB_NAME = os.environ.get("TEST_DB_NAME", "postgres_test")
TEST_DB_USER = os.environ.get("TEST_DB_USER", "postgres_test")
TEST_DB_PASSWORD = os.environ.get("TEST_DB_PASSWORD", "postgres_test")

SMTP_USER = os.getenv("SMTP_USER", "null")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "null")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = os.getenv("SMTP_PORT", "465")

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")
