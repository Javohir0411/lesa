from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import async_session_maker
from db.models import Renter, Rent, Product
from utils.enums import RentStatusEnum, PaymentStatusEnum
from datetime import datetime


async def save_rent_from_fsm(fsm_data: dict):
    async with async_session_maker() as session:  # type: AsyncSession
        # 1️⃣ Renter jadvaliga ma'lumot saqlash
        renter = Renter(
            renter_fullname=fsm_data['renter_fullname'],
            renter_phone_number=fsm_data['renter_phone_number'],
            renter_passport_info=fsm_data.get('passport_info')
        )
        session.add(renter)
        await session.flush()  # ID olish uchun flush qilamiz

        # 2️⃣ Rent jadvaliga ma'lumot saqlash
        for item in fsm_data['rent_info']:
            # Product jadvalidan productni topamiz
            query = select(Product).where(Product.product_type == item['product_type'])
            if 'product_size' in item:
                query = query.where(Product.product_size == item['product_size'])
            result = await session.execute(query)
            product = result.scalar_one_or_none()
            if not product:
                raise ValueError(f"Product topilmadi: {item}")

            rent = Rent(
                renter_id=renter.id,
                product_id=product.id,
                quantity=item['quantity'],
                start_date=datetime.combine(fsm_data['start_date'], datetime.min.time()),
                end_date=datetime.combine(fsm_data['end_date'], datetime.min.time()),
                latitude=fsm_data.get("renter_latitude"),
                longitude=fsm_data.get("renter_longitude"),
                delivery_needed=fsm_data.get('distance_km', 0) > 0,
                delivery_price=fsm_data.get('price_delivery', 0),
                comment=fsm_data.get('notes', ""),
                status=PaymentStatusEnum.not_paid,  # default holat
                rent_status=RentStatusEnum.active
            )
            session.add(rent)

        # 3️⃣ Hammasini commit qilamiz
        await session.commit()
