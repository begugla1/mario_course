from celery import Celery

from utils.celery_tasks import get_dirs_for_celery_tasks
from config import REDIS_URL, API_DIR


celery = Celery(__name__, broker=REDIS_URL, backend=REDIS_URL)

celery.autodiscover_tasks(
    packages=get_dirs_for_celery_tasks(API_DIR, prefix='api'),
    force=True
)
