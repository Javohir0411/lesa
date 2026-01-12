import logging

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from bot_strings.renter_info_strings import RenterInfo
from database.session import get_user_language
from states import RentStatus

router = Router(name=__name__)

PHONE_REGEX = r"^\+998\d{9}$"


@router.message(F.text.regexp(r"^\+998\d{9}$"), RentStatus.renter_phone_number)
async def handle_rent_phone_number(message: types.Message, state: FSMContext):
    renter_phone_number = message.text
    lang = await get_user_language(message)
    await state.update_data(renter_phone_number=renter_phone_number)
    data = await state.get_data()
    logging.info(f"RENTER PHONE NUMBER QO'SHILDI: {data}")
    await state.set_state(RentStatus.renter_passport_info)
    # text = RenterInfo.HOZIRCHA[lang]
    text = RenterInfo.RENTER_PASSPORT_INFO[lang]
    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove(),
    )
