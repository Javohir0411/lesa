from aiogram import Router
from .handle_setting_callback import router as handle_settings_router
from .language import router as language_router

router = Router(name=__name__)

router.include_routers(
    handle_settings_router,
    language_router,
)
