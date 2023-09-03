from celery import Celery


celery = Celery(broker="redis://redis:6379")

celery.autodiscover_tasks()
