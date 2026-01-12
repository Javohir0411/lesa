import logging

from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from database.session import async_session_maker, get_user_language
from keyboards.common_keyboards import build_yes_or_no_kb
from states import RentStatus
from utils.get_user_from_db import get_user_by_telegram_or_phone

router = Router(name=__name__)


@router.message(StateFilter(RentStatus.quantity))
async def handle_product_quantity(message: types.Message, state: FSMContext):
    data = await state.get_data()
    logging.info(f"DATA-DAGI MA'LUMOTLAR: {data}")
    product_quantity = message.text

    lang = await get_user_language(message)

    if lang == "uzl":
        invalid_message = "Iltimos, faqat raqam kiriting!"
        valid_message = "Yana biror mahsulot tanlaysizmi?"

    elif lang == "uzk":
        invalid_message = "Илтимос, фақат рақам киритинг!"
        valid_message = "Яна бирор маҳсулот танлайсизми?"

    elif lang == "rus":
        invalid_message = "Пожалуйста, введите только число!"
        valid_message = "Вы хотели бы выбрать другой товар?"

    if product_quantity.isdigit():

        data = await state.get_data()
        rent_info = data.get("rent_info", [])

        if rent_info:
            # Oxirgi mahsulotga quantity qo‘shamiz
            rent_info[-1]["quantity"] = int(product_quantity)  # raqam sifatida saqlash tavsiya qilinadi
            await state.update_data(rent_info=rent_info)
        logging.info(f"RENT_INFO-DAGI MA'LUMOTLAR: {rent_info}")

        await message.answer(
            text=valid_message,
            reply_markup=build_yes_or_no_kb()
        )
        await state.set_state(RentStatus.additional_choice)

    else:
        await message.answer(
            text=invalid_message,
            reply_markup=types.ReplyKeyboardRemove()
        )
