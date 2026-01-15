import logging

from aiogram.types import ReplyKeyboardRemove

from bot_strings.renter_info_strings import RenterInfo
from database.session import get_user_language
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from states import RentStatus

router = Router(name=__name__)


@router.message(F.text, RentStatus.renter_fullname)
async def handle_renter_fullname(message: types.Message, state: FSMContext):
    renter_fullname = message.text

    data = await state.get_data()
    rent_info = data.get("rent_info", [])
    logging.info(f"rent_info: {rent_info}")

    await state.update_data(rent_info=rent_info, renter_fullname=renter_fullname)
    logging.info(f"RENTER FULLNAME QO'SHILDI: {rent_info}")

    lang = await get_user_language(message)
    text = RenterInfo.RENTER_PHONE_NUMBER[lang]

    await state.set_state(RentStatus.renter_phone_number)
    await message.answer(
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(RentStatus.renter_fullname)
async def handel_invalid_fullname(message: types.Message):
    lang = await get_user_language(message)
    text = RenterInfo.INVALID_RENTER_FULLNAME[lang]
    await message.answer(
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )