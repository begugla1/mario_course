import smtplib

import config
from .utils.email import get_email_template
from celery_app import celery


@celery.task
def send_email(username: str) -> None:
    """
    Sends email to anybody
    """
    email = get_email_template(
        config.SMTP_USER, config.SMTP_USER, "FastAPI Course", username
    )
    with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT) as server:
        server.login(config.SMTP_USER, config.SMTP_PASSWORD)
        server.send_message(email)
