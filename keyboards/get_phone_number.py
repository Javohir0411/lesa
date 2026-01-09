import logging

from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def get_phone_number_kb(state: FSMContext) -> ReplyKeyboardMarkup:
    data = await state.get_data()
    lang = data.get("selected_language")
    logging.info(f"Telefon nomer uchun kelgan lang: {lang}")
    """
    'selected_language': 'uzl'
    'selected_language': 'uzk'
    'selected_language': 'rus'
    """
    builder = ReplyKeyboardBuilder()

    if lang == "uzl":
        builder.button(text="📞 Telefon raqamni yuborish", request_contact=True)
        placeholder = "Kontakt yuborish uchun quyidagi tugmani bosing!"

    elif lang == "uzk":
        builder.button(text="📞 Телефон рақамни юбориш", request_contact=True)
        placeholder = "Контакт юбориш учун қуйидаги тугмани босинг!"

    elif lang == "rus":
        builder.button(text="📞 Отправить номер телефона", request_contact=True)
        placeholder = "Нажмите кнопку ниже, чтобы отправить контакт!"

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder=placeholder)
