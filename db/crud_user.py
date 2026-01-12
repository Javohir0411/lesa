from sqlalchemy.ext.asyncio import AsyncSession
from .models import User


async def create_user(
        db: AsyncSession,
        telegram_id: int,
        user_fullname: str,
        user_phone_number: str,
        selected_language: str
):
    user = User(
        telegram_id=telegram_id,
        user_fullname=user_fullname,
        user_phone_number=user_phone_number,
        selected_language=selected_language
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

