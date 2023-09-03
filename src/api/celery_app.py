from celery import Celery

from config import REDIS_URL


celery = Celery(__name__, broker=REDIS_URL, backend=REDIS_URL)

celery.autodiscover_tasks(['tasks'], force=True)
