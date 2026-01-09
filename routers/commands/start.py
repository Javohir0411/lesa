from keyboards.common_keyboards import build_select_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from utils.enums import LanguageEnum
from aiogram import Router, types
from states import Register
import logging


logging.basicConfig(level=logging.INFO)
router = Router(name=__name__)


@router.message(CommandStart())
async def handle_command_start(message: types.Message, state: FSMContext):
    await state.set_state(Register.language)
    await message.answer(
        text=f"Салом, {message.from_user.full_name}\nКеракли тилни танланг: ",
        reply_markup=build_select_keyboard(LanguageEnum)
    )
    logging.info(f"state: {Register.language} shu yerda boshlandi")
