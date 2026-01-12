import logging

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from bot_strings.rent_command_strings import RentStrings
from database.session import get_user_language
from states import RentStatus

router = Router(name=__name__)


@router.message(F.text, RentStatus.renter_passport_info)
async def handle_renter_passport_info(message: types.Message, state: FSMContext):
    passport_info = message.text
    lang = await get_user_language(message)
    text = RentStrings.GET_RENT_START_DATE[lang]
    await state.update_data(passport_info=passport_info)
    data = await state.get_data()
    logging.info(f"PASSPORT INFO QO'SHILDI: {data}")
    await state.set_state(RentStatus.start_date)
    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove(),
    )