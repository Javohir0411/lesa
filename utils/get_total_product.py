from sqlalchemy import func, select

from database.session import async_session_maker
from db.models import Product


async def get_total_product():
    async with async_session_maker() as session:
        result = await session.execute(
            select(
                Product.product_type,
                Product.product_size,
                func.SUM(Product.total_quantity)
            ).group_by(Product.product_type, Product.product_size)
        )
        return result.all()
