# import logging
#
# from aiogram import Router, F, types
# from aiogram.filters import Command
#
# from bot_strings.leased_command_strings import Leased
# from database.session import get_user_language
# from utils.enums import RentStatusEnum
# from utils.get_leased_rent import get_leased_rents
#
# router = Router(name=__name__)
#
# RENT_STATUS_LABEL = {
#     RentStatusEnum.active: "Ижарада",
#     RentStatusEnum.returned: "Қайтарилган"
# }
#
#
# @router.message(Command("leased", prefix="/!"))
# async def handle_leased_command(message: types.Message):
#     rents = await get_leased_rents()
#     lang = await get_user_language(message)
#     if not rents:
#         text = Leased.NOT_PRODUCT_IN_RENT[lang]
#         await message.answer(text=text)
#         return
#
#     if lang == "uzl":
#         text = "📦 Ijaraga berilgan mahsulotlar:\n\n"
#     elif lang == "uzk":
#         text = "📦 Ижарага берилган маҳсулотлар:\n\n"
#     elif lang == "rus":
#         text = "📦 Продукты в аренду:\n\n"
#
#     # Har bir rentni qo‘shish (tashqarida!)
#     for i, rent in enumerate(rents, start=1):
#         product = rent.product
#         renter = rent.renter
#         size = f" ({product.product_size.value})" if product.product_size else ""
#         status_label = RENT_STATUS_LABEL[rent.rent_status]
#
#         start_date = rent.start_date.strftime("%d-%m-%Y")
#         end_date = rent.end_date.strftime("%d-%m-%Y")
#
#         rent_text = Leased.RESULT[lang].format(
#             rent=rent,
#             renter=renter,
#             status_label=status_label,
#             start_date=start_date,
#             end_date=end_date
#         )
#
#         text += f"<b>{i}) {product.product_type.value}{size}</b>{rent_text}"
#
#     logging.info(f"LEASED RESULT: {text}")
#     await message.answer(text=text)

# leased_handler.py
import logging
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot_strings.leased_command_strings import Leased
from database.session import get_user_language
from utils.enums import RentStatusEnum
from utils.get_leased_rent import get_leased_rents

router = Router(name=__name__)

# Rent status label mapping
RENT_STATUS_LABEL = {
    RentStatusEnum.active: "Ижарада",
    RentStatusEnum.returned: "Қайтарилган"
}

# Pagination
RENT_PER_PAGE = 5  # har sahifada nechta rent ko‘rsatiladi



def build_pagination_keyboard(total_items: int, current_page: int) -> InlineKeyboardMarkup | None:
    total_pages = (total_items + RENT_PER_PAGE - 1) // RENT_PER_PAGE
    buttons = []

    if current_page > 1:
        buttons.append(
            InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"leased_page:{current_page-1}")
        )
    if current_page < total_pages:
        buttons.append(
            InlineKeyboardButton(text="Keyingi ➡️", callback_data=f"leased_page:{current_page+1}")
        )

    if not buttons:
        return None

    return InlineKeyboardMarkup(inline_keyboard=[buttons])



def format_rent_text(rents_slice, lang: str) -> str:
    text = ""
    for i, rent in enumerate(rents_slice, start=1):
        product = rent.product
        renter = rent.renter
        size = f" ({product.product_size.value})" if product.product_size else ""
        status_label = RENT_STATUS_LABEL[rent.rent_status]

        start_date = rent.start_date.strftime("%d-%m-%Y")
        end_date = rent.end_date.strftime("%d-%m-%Y")

        rent_text = Leased.RESULT[lang].format(
            rent=rent,
            renter=renter,
            status_label=status_label,
            start_date=start_date,
            end_date=end_date
        )

        text += f"<b>{i}) {product.product_type.value}{size}</b>{rent_text}"
    return text


@router.message(Command("leased", prefix="/!"))
async def handle_leased_command(message: types.Message):
    rents = await get_leased_rents()
    lang = await get_user_language(message)

    if not rents:
        await message.answer(Leased.NOT_PRODUCT_IN_RENT[lang])
        return

    # Header
    header = {
        "uzl": "📦 Ijaraga berilgan mahsulotlar:\n\n",
        "uzk": "📦 Ижарага берилган маҳсулотлар:\n\n",
        "rus": "📦 Продукты в аренду:\n\n"
    }.get(lang, "📦 Ijaraga berilgan mahsulotlar:\n\n")

    # Birinchi sahifa
    page = 1
    start_idx = (page - 1) * RENT_PER_PAGE
    end_idx = start_idx + RENT_PER_PAGE
    rents_slice = rents[start_idx:end_idx]

    text = header + format_rent_text(rents_slice, lang)
    kb = build_pagination_keyboard(total_items=len(rents), current_page=page)

    await message.answer(text=text, reply_markup=kb, parse_mode="HTML")


@router.callback_query(lambda c: c.data.startswith("leased_page:"))
async def handle_leased_pagination(callback: CallbackQuery):
    rents = await get_leased_rents()
    lang = await get_user_language(callback.message)

    page = int(callback.data.split(":")[1])
    start_idx = (page - 1) * RENT_PER_PAGE
    end_idx = start_idx + RENT_PER_PAGE
    rents_slice = rents[start_idx:end_idx]

    header = {
        "uzl": "📦 Ijaraga berilgan mahsulotlar:\n\n",
        "uzk": "📦 Ижарага берилган маҳсулотлар:\n\n",
        "rus": "📦 Продукты в аренду:\n\n"
    }.get(lang, "📦 Ijaraga berilgan mahsulotlar:\n\n")

    text = header + format_rent_text(rents_slice, lang)
    kb = build_pagination_keyboard(total_items=len(rents), current_page=page)

    await callback.message.edit_text(text=text, reply_markup=kb, parse_mode="HTML")
    await callback.answer()
