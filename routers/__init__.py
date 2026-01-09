__all__ = ("router",)

from aiogram import Router
from .commands import router as command_router
from .register_user_handlers import router as register_user_router

router = Router(name=__name__)

router.include_routers(
    command_router,
    register_user_router,
)
