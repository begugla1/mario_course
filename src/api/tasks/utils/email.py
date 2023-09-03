from email.message import EmailMessage

import config


def get_email_template(
    from_addr: str,
    to_addr: str,
    subject: str = "",
    username: str = "",
        ) -> EmailMessage:
    """
    Generates email template
    """
    email = EmailMessage()
    email["Subject"] = subject
    email["From"] = from_addr
    email["To"] = to_addr

    email.set_content(f"Hello there, {username}! I\'m {config.SMTP_USER}!")

    return email
