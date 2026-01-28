import asyncio
from database.session import async_session_maker
from db.models import Product
from utils.enums import ProductTypeEnum, LesaSizeEnum


async def add_products():
    async with async_session_maker() as session:
        products = [
            # Lesa mahsulotlari, har biri o'z kattaligi bilan
            Product(
                product_type=ProductTypeEnum.lesa,
                product_size=LesaSizeEnum.katta,
                total_quantity=273,
                price_per_day=3000
            ),
            Product(
                product_type=ProductTypeEnum.lesa,
                product_size=LesaSizeEnum.orta,
                total_quantity=50,
                price_per_day=20000
            ),
            Product(
                product_type=ProductTypeEnum.lesa,
                product_size=LesaSizeEnum.kichik,
                total_quantity=50,
                price_per_day=12000
            ),

            # Boshqa mahsulotlar, product_size = None
            Product(
                product_type=ProductTypeEnum.monolit,
                product_size=None,
                total_quantity=20,
                price_per_day=5000
            ),
            Product(
                product_type=ProductTypeEnum.taxta,
                product_size=None,
                total_quantity=300,
                price_per_day=1500
            ),
        ]

        session.add_all(products)
        await session.commit()
        print("Barcha product-lar bazaga qo'shildi!")


if __name__ == "__main__":
    asyncio.run(add_products())
