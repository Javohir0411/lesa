from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot_strings.rent_command_strings import RentStrings
from database.session import async_session_maker, get_user_language
from keyboards.common_keyboards import build_select_keyboard, build_lesa_keyboard
# from keyboards.select_product_keyboard import build_products_reply_keyboard
from states import RentStatus
from utils.enums import ProductTypeEnum, LesaSizeEnum
from utils.get_user_from_db import get_user_by_telegram_or_phone

router = Router(name=__name__)


@router.message(RentStatus.product_choice)
async def handle_selected_product(message: types.Message, state: FSMContext):
    selected_product = message.text
    lang = await get_user_language(message)

    if selected_product not in [product_type.value for product_type in ProductTypeEnum]:
        # kb = await build_products_reply_keyboard(message)
        await message.reply(
            text="Iltimos, faqat quyidagi tugmalardan tanlang.",
            reply_markup=build_select_keyboard(ProductTypeEnum)
        )
        return

    data = await state.get_data()
    rent_info = data.get("rent_info", [])

    rent_info.append({
        "product_type": selected_product,
    })
    await state.update_data(rent_info=rent_info)

    quantity_string = RentStrings.INSERT_QUANTITY_PRODUCT[lang]

    if selected_product == ProductTypeEnum.lesa.value:
        await state.set_state(RentStatus.lesa_size_choice)
        if lang == "uzl":
            size = "Iltimos, lesa uchun o'lcham kiriting:"
        elif lang == "uzk":
            size = "Илтимос, леса учун ўлчам киритинг:"
        elif lang == "rus":
            size = "Пожалуйста, укажите размер лесы:"

        await message.answer(
            text=size,
            reply_markup=build_lesa_keyboard(lang)
        )


    else:
        # Monolit yoki Taxta → miqdor kiritish
        await state.set_state(RentStatus.quantity)
        await message.answer(
            text=quantity_string,
            reply_markup=ReplyKeyboardRemove()
        )
