from database import session
from keyboards.common_keyboards import build_select_keyboard
from bot_strings.rent_command_strings import RentStrings
from database.session import get_user_language, async_session_maker
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router, types
import logging
from database.products.available_product import get_available_products

from states import RentStatus
from utils.enums import ProductTypeEnum

logging.basicConfig(level=logging.DEBUG)
router = Router(name=__name__)


@router.message(Command("rent", prefix="/!"))
async def handle_command_rent(message: types.Message, state: FSMContext):
    logging.info("HANDLE COMMAND RENT ISHGA TUSHDI")

    lang = await get_user_language(message)
    logging.info(f"COMMAND RENT UCHUN KELGAN TIL: {lang}")

    async with async_session_maker() as session:
        available_products = await get_available_products(session)

    message_text = RentStrings.RENT_STARTING_PROCESS[lang]
    for product, remaining_quantity in available_products:
        if product.product_type.name == ProductTypeEnum.lesa.name:
            size_name = product.product_size.name
            product_name = RentStrings.CHOOSE_PRODUCT_KEYBOARD[lang][ProductTypeEnum.lesa.name][size_name]
        else:
            product_name = RentStrings.CHOOSE_PRODUCT_KEYBOARD[lang][product.product_type.name]

        # real-time qoldiqni chiqaramiz
        if lang == "uzl":
            message_text += f"<b>{product_name}</b> - Qoldiq: {remaining_quantity}\n"
        elif lang == "uzk":
            message_text += f"{product_name} - Қолдиқ: {remaining_quantity}\n"
        elif lang == "rus":
            message_text += f"{product_name} - Остаток: {remaining_quantity}\n"

    logging.info(f"MESSAGE TEXT: {message_text}")
    #
    # await state.set_state(RentStatus.lesa_size_choice)

    await state.set_state(RentStatus.product_choice)
    await message.answer(
        text=message_text,
        reply_markup=build_select_keyboard(ProductTypeEnum),
    )
