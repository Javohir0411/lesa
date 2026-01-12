from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
import logging
from bot_strings.rent_command_strings import RentStrings
from bot_strings.renter_info_strings import RenterInfo
from database.products.available_product import get_available_products
from database.session import async_session_maker, get_user_language
from db.models import Renter
from keyboards.common_keyboards import build_select_keyboard, build_yes_or_no_kb
from states import RentStatus
from utils.enums import ProductTypeEnum
from utils.get_user_from_db import get_user_by_telegram_or_phone

logging.basicConfig(level=logging.INFO)
router = Router(name=__name__)


@router.message(RentStatus.additional_choice,
                F.text.casefold() == "yes")  # user yes/ha deb javob bersa
async def handle_additional_choice_ok(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id

    async with async_session_maker() as session:
        user = await get_user_by_telegram_or_phone(
            db=session,
            telegram_id=telegram_id,
        )
        lang = user.selected_language if user else "uzk"
        available_products = await get_available_products(session)

    await state.update_data(additional_choice=True)
    await state.set_state(RentStatus.product_choice)

    text = RentStrings.CHOOSE_ANOTHER_PRODUCT[lang]
    for product in available_products:
        # Lesa mahsulotlarini tilga mos olish
        if product.product_type.name == ProductTypeEnum.lesa.name:
            size_name = product.product_size.name
            product_name = RentStrings.CHOOSE_PRODUCT_KEYBOARD[lang][ProductTypeEnum.lesa.name][size_name]
        else:
            product_name = RentStrings.CHOOSE_PRODUCT_KEYBOARD[lang][product.product_type.name]

        # Qoldiqni tilga mos qo‘shish
        if lang == "uzl":
            text += f"<b>{product_name}</b> - Qoldiq: {product.total_quantity}\n"
        elif lang == "uzk":
            text += f"{product_name} - Қолдиқ: {product.total_quantity}\n"
        elif lang == "rus":
            text += f"{product_name} - Остаток: {product.total_quantity}\n"

    logging.info(f"MESSAGE TEXT: {text}")
    data = await state.get_data()
    logging.info(f"DATA: {data}")

    await message.answer(
        text=text,
        reply_markup=build_select_keyboard(ProductTypeEnum),
    )


@router.message(
    RentStatus.additional_choice,
    F.text.casefold() == "no"
)  # user no/yo'q deb javob bersa
async def handle_additional_choice_not_ok(message: types.Message, state: FSMContext):
    await state.update_data(additional_choice=False)
    lang = await get_user_language(message)

    text = RentStrings.ASK_RENTER_FULLNAME[lang]
    await state.set_state(RentStatus.renter_fullname)
    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(RentStatus.additional_choice)  # user no | yes javoblarini tanlamasa
async def handle_additional_choice_could_not_understand(message: types.Message):
    lang = await get_user_language(message)
    text = RentStrings.INVALID_YES_NO[lang]
    await message.answer(
        text=text,
        reply_markup=build_yes_or_no_kb(),
    )
