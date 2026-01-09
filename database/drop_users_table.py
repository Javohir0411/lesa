import asyncio
from database.session import engine
import logging
from sqlalchemy import text

logging.basicConfig(level=logging.INFO)


async def drop_users_table():
    async with engine.begin() as conn:
        # SQL orqali faqat users jadvalini o'chiramiz
        await conn.execute(text("DROP TABLE IF EXISTS users CASCADE;"))
        # Agar CASCADE bo'lsa, unga bo'lgan cheklovlar ham o'chadi
    logging.info("User jadvali o'chirildi ❌")

if __name__ == "__main__":
    asyncio.run(drop_users_table())
