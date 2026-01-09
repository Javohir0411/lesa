import logging

from sqlalchemy import select  # ma'lumotni olish degan buyruq
# from db.models import Product


async def get_products_from_db(session):
    result = await session.execute(select(Product))  # Jadvaldan ma'lumotlarni barcha olish
    raw = result.scalars().all()  # scalar() Product-dagi barcha obyektni olib berdi, all() list qildi
    logging.info(f"GET PRODUCT FROM DB: {raw}")
    return raw
