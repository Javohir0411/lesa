import logging
from aiogram.filters import StateFilter

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot_strings.rent_command_strings import RentStrings
from database.session import async_session_maker, get_user_language
from keyboards.common_keyboards import build_select_keyboard, build_lesa_keyboard
from states import RentStatus
from utils.enums import LesaSizeEnum
from utils.get_user_from_db import get_user_by_telegram_or_phone

router = Router(name=__name__)


@router.message(StateFilter(RentStatus.lesa_size_choice))
async def handle_selected_size(message: types.Message, state: FSMContext):
    selected_size = message.text
    lang = await get_user_language(message)
    text_size = RentStrings.INSERT_INVALID_SIZE[lang]
    text_quantity = RentStrings.INSERT_QUANTITY_PRODUCT[lang]

    text_to_enum = {RentStrings.LESA_SIZE_TRANSLATION[lang][e]: e.value for e in LesaSizeEnum}

    if selected_size in text_to_enum:
        enum_value = text_to_enum[selected_size]

        data = await state.get_data()
        rent_info = data.get("rent_info", [])

        if rent_info:
            # Oxirgi mahsulotga size qo'shamiz
            rent_info[-1]["product_size"] = enum_value
            await state.update_data(rent_info=rent_info)

        await state.set_state(RentStatus.quantity)
        await message.answer(text=text_quantity, reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text=text_size, reply_markup=build_lesa_keyboard(lang))
