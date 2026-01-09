from sqlalchemy import select, or_
from db.models import User
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_by_telegram_or_phone(
        db: AsyncSession,
        telegram_id: int = None,
        phone_number: str = None,
):
    result = await db.execute(
        select(User).where(
            or_(
                User.telegram_id == telegram_id if telegram_id else False,
                User.user_phone_number == phone_number if phone_number else False,
            )
        )
    )
    return result.scalar_one_or_none()


"""
from sqlalchemy import select

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()  # scalars() → faqat User obyekti
    return users
    
    Barcha user-larni olish
"""
