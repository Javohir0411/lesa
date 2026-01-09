import logging

from sqlalchemy import func, select
from db.models import Product, Rent
from utils.enums import RentStatusEnum

logging.basicConfig(level=logging.INFO)


async def get_available_products(session):
    products = await session.execute(select(Product))  # Bazadan barcha Products-ni oldi
    products = products.scalars().all()  # Olingan barcha Products-ni qaytaryapti

    available_products = []
    for product in products:
        rented = await session.execute(
            select(func.coalesce(func.sum(Rent.quantity), 0))
            # barcha ijaraga berilganlarni hisoblash, berilmagan bo'lsa, 0

            .where(Rent.product_id == product.id)
            # qachonki ijaraga berilgan mahsulot bilan kelayotgan mahsulotni id raqami teng bo'lsa

            .where(Rent.rent_status == RentStatusEnum.active)
            # qachonki ijara status teng bo'lsa, active-ga
        )
        rented_quantity = rented.scalar() or 0
        # rented_quantity(ijaraga berilganlar soni) tenglashtirildi umumiy hisoblangan songa yoki 0 ga

        if product.total_quantity - rented_quantity > 0:  # umumiy miqdordan ijaraga berilganlarni ayirganda 0 dan katta bo'lsa
            available_products.append(product)  # listga qo'shamiz

    logging.info(f"GET AVAILABLE PRODUCTS: {available_products}")
    return available_products
