from aiogram import Router
from .get_fullname import router as fullname_router
from .get_selected_language import router as language_router
from .get_phone_number import router as phone_number_router

router = Router(name=__name__)

router.include_routers(
    fullname_router,
    language_router,
    phone_number_router,
)
