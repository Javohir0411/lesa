import asyncio
from db.models import User
from database.base import Base
from database.session import engine
import logging

logging.basicConfig(level=logging.INFO)


async def init_models():
    async with engine.begin() as conn:  # bazaga bog'lanishin boshlash, async with esa ish tugagach ulanishin avtomatik yopish
        await conn.run_sync(Base.metadata.create_all)
        # await conn.run_sync(Base.metadata.drop_all)

        """
        Base.metadata.create_all — Base ichidagi barcha jadvallarni yaratadi.
        Base.metadata.drop_all - Base ichidagi barcha jadvallarni o'chiradi.
        await conn.run_sync(...) — “Python kutib tur, bazaga bu buyruqni yuborib, javobni ol” degani.
        """
    logging.info("Jadval(lar) yaratildi ✅")
    # logging.info("Jadval(lar) o'chirildi ✅")


if __name__ == "__main__":
    asyncio.run(init_models()) # asyncio.run(...) asinxron funksiyalarni ishga tushiradi
