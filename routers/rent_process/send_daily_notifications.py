import logging
from datetime import date

from aiogram import Bot
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database.session import async_session_maker
from db.models import Rent, User
from utils.enums import RentStatusEnum

logging.basicConfig(level=logging.INFO)

labels = {
    "uzl": {
        "product_price": "Mahsulot narxi",
        "delivery": "Yetkazib berish",
        "payment_status": "To'lov holati",
        "total_product": "Umumiy mahsulot narxi",
        "total_delivery": "Umumiy yetkazib berish",
        "total_sum": "Umumiy summa",
        "location": "Manzil",
        "phone_number": "Telefon raqam",
        "passport": "Passport",
        "notes": "Qo‘shimcha"
    },
    "uzk": {
        "product_price": "Маҳсулот нархи",
        "delivery": "Етказиб бериш",
        "payment_status": "Тўлов ҳолати",
        "total_product": "Умумий маҳсулот нархи",
        "total_delivery": "Умумий етказиб бериш",
        "total_sum": "Умумий сумма",
        "location": "Манзил",
        "phone_number": "Телефон рақам",
        "passport": "Паспорт",
        "notes": "Қўшимча"
    },
    "rus": {
        "product_price": "Цена товара",
        "delivery": "Доставка",
        "payment_status": "Статус оплаты",
        "total_product": "Общая цена товаров",
        "total_delivery": "Общая доставка",
        "total_sum": "Общая сумма",
        "location": "Адрес",
        "phone_number": "Номер телефона",
        "passport": "Паспорт",
        "notes": "Дополнительно"
    }
}


async def get_user_language_by_user_id(telegram_id: int, session: AsyncSession) -> str:
    result = await session.execute(select(User).where(User.telegram_id == telegram_id))
    user = result.scalar_one_or_none()
    return user.selected_language if user else "rus"


async def send_expired_rent_notification(bot: Bot):
    today = date.today()
    async with async_session_maker() as session:
        result = await session.execute(
            select(Rent)
            .options(
                selectinload(Rent.product),  # product relationship oldindan yuklanadi
                selectinload(Rent.renter),  # renter relationship oldindan yuklanadi
                selectinload(Rent.user),
            )
            .where(
                and_(
                    Rent.end_date <= today,
                    Rent.rent_status == RentStatusEnum.active
                )
            )
        )
        rents = result.scalars().all()
        if not rents:
            logging.info("BUGUN TUGAGAN IJARA TOPILMADI")
            return

        renters_dict = {}
        for rent in rents:
            renters_dict.setdefault(rent.renter_id, []).append(rent)

        for renter_id, rents_list in renters_dict.items():
            user = rents_list[0].user
            lang = user.selected_language if user else "uzk"

            headers = {
                "uzl": f"🕖 {rents_list[0].renter.renter_fullname} ijaraga olgan mahsulotlar muddati bugun tugadi \n\n",
                "uzk": f"🕖 {rents_list[0].renter.renter_fullname} ижарага олган маҳсулотлар муддати бугун тугади \n\n",
                "rus": f"🕖 {rents_list[0].renter.renter_fullname} срок действия арендованных продуктов истекает сегодня: \n\n",
            }
            # tilga mos label

            text = headers[lang]
            lbl = labels[lang]
            total_product_price = 0
            total_delivery_price = 0
            total_sum = 0

            for rent in rents_list:
                line = f"{rent.product.product_type}"

                if rent.product.product_size:
                    line += f" ({rent.product.product_size})"

                line += f" — {rent.quantity} dona\n"
                line += f"{lbl['product_price']}: {rent.product_price} so'm\n"

                line += f"{lbl['delivery']}: {rent.delivery_price} so'm\n"
                logging.info(f"TOTAL DELIVERY: {rent.delivery_price} so'm")

                line += f"{lbl['payment_status']}: {rent.status}\n\n"

                text += line  # 🔥 MUHIM QATOR

                total_product_price += rent.product_price or 0

            total_delivery_price += rent.delivery_price or 0
            total_sum = total_product_price + total_delivery_price

            text += f"\n{lbl['total_product']}: {total_product_price} so'm\n"
            text += f"{lbl['total_delivery']}: {total_delivery_price} so'm\n"
            text += f"{lbl['total_sum']}: {total_sum} so'm\n"

            text += f"📍{lbl['location']}: {rents_list[0].latitude}, {rents_list[0].longitude}\n"
            text += f"📍{lbl['phone_number']}: {rents_list[0].renter.renter_phone_number}\n"
            text += f"🛂 {lbl['passport']}: {rents_list[0].renter.renter_passport_info}\n"
            text += f"📝 {lbl['notes']}: {rents_list[0].comment}"

            try:
                await bot.send_message(chat_id=1891727351, text=text)
            except Exception as e:
                logging.error(f"XABAR YUBORISHDA XATOLIK: {e}")
