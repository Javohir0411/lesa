from aiogram import Router, F, types
from datetime import datetime

from aiogram.fsm.context import FSMContext

from bot_strings.rent_command_strings import RentStrings
from database.session import get_user_language
# from keyboards.common_keyboards import build_location_type_kb
from states import RentStatus
import logging

from utils.filter_date import is_date

logging.basicConfig(level=logging.INFO)
router = Router(name=__name__)


@router.message(F.text.func(is_date), RentStatus.start_date)
async def handle_rent_start_date(message: types.Message, state: FSMContext):
    start_date = datetime.strptime(message.text, "%d.%m.%Y").date()
    await state.update_data(start_date=start_date)
    data = await state.get_data()
    logging.info(f"START DATE QO'SHILDI: {data}")
    logging.info(f"START DATE QO'SHILDI: {data['start_date']}")
    lang = await get_user_language(message)
    text = RentStrings.GET_RENT_END_DATE[lang]
    await state.set_state(RentStatus.end_date)
    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(F.text.func(is_date), RentStatus.end_date)
async def handle_rent_end_date(message: types.Message, state: FSMContext):
    end_date = datetime.strptime(message.text, "%d.%m.%Y").date()
    await state.update_data(end_date=end_date)
    data = await state.get_data()
    logging.info(f"END DATE QO'SHILDI: {data}")
    logging.info(f"END DATE QO'SHILDI: {data['end_date']}")
    lang = await get_user_language(message)
    text = RentStrings.LOCATION_REQUEST[lang]
    await state.set_state(RentStatus.location_request)
    await message.answer(
        text=text,
        # reply_markup=build_location_type_kb(lang)
    )
