import os
import uuid

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase

from .models import User, get_user_db

SECRET = os.environ.get("JWT_SECRET", "undefined-secret")


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, request: Request | None = None
            ):
        print(f"User {user.id} has registered.")


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db)
        ):
    yield UserManager(user_db)


cookie_transport = CookieTransport("auth-token", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

get_current_active_user = fastapi_users.current_user(active=True)
