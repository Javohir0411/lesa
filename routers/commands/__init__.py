from .start import router as start_router
from .help import router as help_router
from .rent import router as rent_router
from .leased import router as leased_router
from aiogram import Router

router = Router(name=__name__)

router.include_routers(
    start_router,
    help_router,
    rent_router,
    leased_router,
)
