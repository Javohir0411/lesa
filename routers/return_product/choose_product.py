from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database.session import get_user_language, async_session_maker
from db.models import Rent, Product
from states import ReturnProduct
from utils.enums import RentStatusEnum

router = Router(name=__name__)


@router.message(ReturnProduct.choosing_product)
async def product_selected(message: types.Message, state: FSMContext):
    lang = await get_user_language(message)
    product_text = message.text  # misol: "Lesa | katta (10)"
    data = await state.get_data()
    renter_id = data["renter_id"]

    async with async_session_maker() as session:
        result = await session.execute(
            select(Rent)
            .options(selectinload(Rent.product))  # Product-ni oldindan yuklaymiz
            .where(Rent.renter_id == renter_id)
            .where(Rent.rent_status == RentStatusEnum.active)
        )
        active_rents = result.scalars().all()

        # Tanlangan mahsulotni aniqlash
        rent = None
        for r in active_rents:
            size = f" | {r.product.product_size}" if r.product.product_size else ""
            key_text = f"{r.product.product_type}{size} ({r.quantity})"
            if key_text == product_text:
                rent = r
                break

        if not rent:
            await message.answer("Маҳсулот топилмади, қайта уриниб кўринг.")
            return

        await state.update_data(rent_id=rent.id)
        await message.answer(
            {
                "uzl": f"Qancha mahsulot qaytarildi? (max {rent.quantity})",
                "uzk": f"Қанча маҳсулот қайтарилди? (max {rent.quantity})",
                "rus": f"Сколько товаров было возвращено? (max {rent.quantity})",
            }[lang],
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.set_state(ReturnProduct.entering_quantity)
