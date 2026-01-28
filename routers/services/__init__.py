from aiogram import Router
from .reports import router as reports_router
router = Router(name=__name__)

router.include_routers(
    reports_router,
)