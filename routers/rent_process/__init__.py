from .handel_renter_fullname import router as renter_fullname_router
from .handle_renter_phone_number import router as renter_phone_number_router
from .handle_renter_passport_info import router as renter_passport_info
from .handle_start_end_date import router as start_end_date_router
from .location import router as location_router
from .handle_notes_for_renter import router as notes_for_renter_router
from aiogram import Router

router = Router(name=__name__)

router.include_routers(
    renter_fullname_router,
    renter_phone_number_router,
    renter_passport_info,
    start_end_date_router,
    location_router,
    notes_for_renter_router,
)
