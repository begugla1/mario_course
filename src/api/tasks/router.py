from fastapi import APIRouter, Depends

from auth.models import User
from auth.users import get_current_active_user
from .tasks import send_email
from .schemas import EmailOutputMessage


router = APIRouter(prefix="/user")


@router.get("/email")
def get_email(
    user: User = Depends(get_current_active_user)
        ) -> EmailOutputMessage:
    send_email(user.email)
