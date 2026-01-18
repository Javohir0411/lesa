from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database.session import get_user_language, async_session_maker
from db.models import Renter, Rent
from keyboards.common_keyboards import build_select_keyboard
from states import ReturnProduct
from utils.enums import RentStatusEnum, ProductTypeEnum

router = Router(name=__name__)


@router.message(F.text, ReturnProduct.choosing_renter)
async def handle_choosing_renter(message: types.Message, state: FSMContext):
    lang = await get_user_language(message)
    renter_name = message.text
    async with async_session_maker() as session:
        result = await session.execute(
            select(Renter)
            .options(
                selectinload(Renter.rents)
                .selectinload(Rent.product)  # 🔑 SHU TARZDA
            )
            .where(Renter.renter_fullname == renter_name)
        )
        renter = result.scalar_one_or_none()
        if not renter:
            await message.answer(
                {
                    "uzl": "Bunday ijarachi topilmadi, qayta urinib ko'ring",
                    "uzk": "Бундай ижарачи топилмади, қайта уриниб кўринг",
                    "rus": "Арендатора не найдено, пожалуйста, попробуйте еще раз.",
                }[lang]
            )
            return

        active_rents = [r for r in renter.rents if r.rent_status == RentStatusEnum.active]

        if not active_rents:
            await message.answer(
                {
                    "uzl": "Bu ijarachida faol ijara mavjud emas",
                    "uzk": "Bu ijarachida faol ijara mavjud emas",
                    "rus": "У данного арендатора нет действующего договора аренды.",
                }[lang]
            )
            return

        items = []
        for r in active_rents:
            p = r.product
            if p.product_type == ProductTypeEnum.lesa:
                items.append(f"{p.product_type.value} | {p.product_size.value} ({r.quantity})")
            else:
                items.append(f"{p.product_type.value} ({r.quantity})")

        kb = build_select_keyboard(items)

        await state.update_data(renter_id=renter.id)
        await state.set_state(ReturnProduct.choosing_product)
        await message.answer(
            {
                "uzl": "Qaytariladigan mahsulotni tanlang: ",
                "uzk": "Қайтариладиган маҳсулотни танланг: ",
                "rus": "Выберите товар для возврата: ",
            }[lang],
            reply_markup=kb,
        )
