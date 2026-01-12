from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from database.config import settings
from utils.get_user_from_db import get_user_by_telegram_or_phone

DATABASE_URL = settings.DATABASE_URL
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


async def get_user_language(message) -> dict:
    telegram_id = message.from_user.id
    async with async_session_maker() as session:
        user = await get_user_by_telegram_or_phone(
            db=session,
            telegram_id=telegram_id,
        )
        lang = user.selected_language if user else "uzk"
        return lang
