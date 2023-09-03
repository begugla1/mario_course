from fastapi import APIRouter

from .tasks import send_email
from .schemas import EmailOutputMessage


router = APIRouter(prefix="/user")


@router.get("/email")
def get_email(
    user: str
        ) -> EmailOutputMessage:
    send_email.delay(user)
    return EmailOutputMessage(status="Delievered", message="Goodluck!")
