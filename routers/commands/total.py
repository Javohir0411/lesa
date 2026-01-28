from aiogram import Router, types
from aiogram.filters import Command

from database.session import get_user_language
from utils.admin_only import AdminOnly
from utils.get_total_product import get_total_product

router = Router(name=__name__)

PRODUCT_TYPE_TRANSLATIONS = {
    "uzl": {"lesa": "Леса", "monolit": "Монолит устун", "taxta": "Тахта"},
    "uzk": {"lesa": "Леса", "monolit": "Монолит устун", "taxta": "Тахта"},
    "rus": {"lesa": "Леса", "monolit": "Монолит", "taxta": "Доска"},
}


@router.message(AdminOnly(), Command("total", prefix="/!"))
async def handle_total_command(message: types.Message):
    lang = await get_user_language(message)
    totals = await get_total_product()
    if not totals:
        await message.answer(
            {
                "uzl": "Hozircha mahsulotlar mavjud emas.",
                "uzk": "Ҳозирча маҳсулотлар мавжуд эмас.",
                "rus": "Пока нет доступных товаров."
            }[lang])
        return

    text = {
        "uzl": "📦 Umumiy mahsulotlar:\n\n",
        "uzk": "📦 Умумий маҳсулотлар:\n\n",
        "rus": "📦 Общие товары:\n\n"
    }[lang]

    for product_type, product_size, total_quantity in totals:
        type_text = PRODUCT_TYPE_TRANSLATIONS[lang].get(product_type, product_type)
        size_text = f" ({product_size})" if product_size else ""
        text += f"<b>{type_text}</b>{size_text}:  <u>{total_quantity}</u>\n"

    await message.answer(text)

@router.message(Command("total", prefix="/!"))
async def handle_total_command_not_admin(message: types.Message):
    lang = await get_user_language(message)
    await message.answer(
        {
            "uzl": "Sizga ruxsat yo'q ❌\nMa'lumotlar faqat admin uchun",
            "uzk": "Сизга рухсат йўқ ❌\nМаълумотлар фақат админ учун",
            "rus": "Вам запрещено ❌\nИнформация только для администратора.",
        }.get(lang, "Сизга рухсат йўқ ❌\nМаълумотлар фақат админ учун")
    )