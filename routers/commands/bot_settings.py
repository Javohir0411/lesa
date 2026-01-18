import logging

from aiogram import Router, F, types
from aiogram.filters import Command

from database.session import get_user_language
from keyboards.inlinekeyboard.build_settings_button import build_settings_button

router = Router(name=__name__)


@router.message(Command("settings", prefix="/!"))
async def handle_command_settings(message: types.Message):
    lang = await get_user_language(message)
    logging.info(f"SETTINGS LANGUAGE : {lang}")
    kb = build_settings_button(lang)
    await message.answer(
        text={
            "uzl": "⚙️ Sozlamalarni tanlang: ",
            "uzk": "⚙️ Созламаларни танланг: ",
            "rus": "⚙️ Выберите настройки: ",
        }[lang],
        reply_markup=kb,
    )
