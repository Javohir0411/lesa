from keyboards.select_product_keyboard import build_products_reply_keyboard
from bot_strings.rent_command_strings import RentStrings
from database.session import async_session_maker
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router, types
import logging

from states import RentStatus
from utils.enums import RentStatusEnum
from utils.get_user_from_db import get_user_by_telegram_or_phone

logging.basicConfig(level=logging.DEBUG)
router = Router(name=__name__)


@router.message(Command("rent", prefix="/!"))
async def handle_command_rent(message: types.Message, state: FSMContext):
    logging.info("HANDLE COMMAND RENT ISHGA TUSHDI")

    telegram_id = message.from_user.id

    logging.info("USER BAZADAN IZLANYAPTI")
    async with async_session_maker() as session:
        user = await get_user_by_telegram_or_phone(
            db=session,
            telegram_id=telegram_id,
        )

    lang = user.selected_language if user else "uzk"
    logging.info(f"COMMAND RENT UCHUN KELGAN TIL: {lang}")

    message_text = RentStrings.RENT_STARTING_PROCESS[lang]
    logging.info(f"MESSAGE TEXT: {message_text}")

    keyboard = await build_products_reply_keyboard()

    await state.set_state(RentStatus.product_choice)
    await message.answer(
        text=message_text,
        reply_markup=keyboard,
    )
