from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove

from bot_strings.help_command_strings import HelpStrings
from database.session import async_session_maker
from utils.enums import LanguageEnum
import logging

from utils.get_user_from_db import get_user_by_telegram_or_phone

logging.basicConfig(level=logging.INFO)
router = Router(name=__name__)


@router.message(Command("help", prefix="/!"))
async def handle_command_help(message: types.Message):
    logging.info(f"{message.text} COMMAND ISHINI BOSHLADI")
    telegram_id = message.from_user.id

    async with async_session_maker() as session:
        user = await get_user_by_telegram_or_phone(
            db=session,
            telegram_id=telegram_id,
        )

    lang = user.selected_language if user else "uzk"

    message_text = HelpStrings.TEXT.get(lang, HelpStrings.TEXT["uzk"])

    await message.answer(
        text=message_text,
        reply_markup=ReplyKeyboardRemove()
    )
    logging.info(f"{message.text} COMMAND ISHINI YAKUNLADI")
