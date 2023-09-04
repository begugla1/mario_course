import smtplib

import global_config
from .utils.email import get_email_template
from celery_app import celery


@celery.task
def send_email(username: str) -> None:
    """
    Sends email to anybody
    """
    email = get_email_template(
        global_config.SMTP_USER, global_config.SMTP_USER, "FastAPI Course",
        username
    )
    with smtplib.SMTP_SSL(
        global_config.SMTP_HOST, global_config.SMTP_PORT
            ) as server:
        server.login(global_config.SMTP_USER, global_config.SMTP_PASSWORD)
        server.send_message(email)
