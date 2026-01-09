from database.products.available_product import get_available_products
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from database.session import async_session_maker
from db.models import RentStatusEnum


async def build_products_reply_keyboard():
    async with async_session_maker() as session:
        available_products = await get_available_products(session)

        builder = ReplyKeyboardBuilder()
        for product in available_products:
            text = f"{product.product_type.value}"
            if product.product_size:
                text += f" ({product.product_size.value})"
            # available_products allaqachon qoldiq > 0 bo‘lgan mahsulotlar
            text += f" - Qoldiq: {product.total_quantity}"  # optional, yoki oldin hisoblangan qoldiq

            builder.button(text=text)

        builder.adjust(1)
        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
