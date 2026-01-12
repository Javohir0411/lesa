from aiogram import Router, types
# from .handle_location_type import router as location_type_router
from .handle_map_location import router as map_location_router

router = Router(name=__name__)

router.include_routers(
    map_location_router,
)
