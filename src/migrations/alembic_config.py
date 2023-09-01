import sys
import os


sys.path.append("/code/src/api")

DB_HOST: str = os.environ.get("DB_HOST", "database")
DB_PORT: str = os.environ.get("DB_PORT", "5432")
DB_NAME: str = os.environ.get("DB_NAME", "postgres")
DB_USER: str = os.environ.get("DB_USER", "postgres")
DB_PASSWORD: str = os.environ.get("DB_PASSWORD", "postgres")
