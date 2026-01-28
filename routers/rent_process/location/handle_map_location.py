import logging

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from bot_strings.rent_command_strings import RentStrings
from database.session import get_user_language
from keyboards.common_keyboards import build_yes_or_no_kb
from states import RentStatus
from utils.haversine import haversine

logging.basicConfig(level=logging.INFO)
router = Router(name=__name__)


def calculate_price(distance_km):
    base = 30000
    extra_per_km = 5000

    if distance_km <= 2.5:
        return base * 2

    else:
        extra_km = distance_km - 2.5
        total_price = (base + extra_km * extra_per_km) * 2

    return total_price


@router.message(F.location, RentStatus.location_request)
async def handle_location_request(message: types.Message, state: FSMContext):
    location = message.location

    renter_latitude = location.latitude
    renter_longitude = location.longitude

    # 📍 1️⃣ Doimiy nuqta (ombor / baza)
    base_latitude = 41.425701
    base_longitude = 69.343535

    distance_km = haversine(
        base_latitude,
        base_longitude,
        renter_latitude,
        renter_longitude,
    )

    distance_km = round(distance_km, 2)

    price_delivery = calculate_price(distance_km)

    await state.update_data(
        renter_latitude=renter_latitude,
        renter_longitude=renter_longitude,
        distance_km=distance_km,
        price_delivery=price_delivery,
    )

    data = await state.get_data()
    logging.info(f"DATA-NI MA'LUMOTLARI: {data}")
    lang = await get_user_language(message)
    text = RentStrings.SENT_LOCATION_INFO[lang].format(
        renter_latitude=renter_latitude,
        renter_longitude=renter_longitude,
        distance_km=distance_km,
        price_delivery=price_delivery,
    )

    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove()
    )

    if lang == "uzl":
        text = ("Mijoz haqida, qo'shimcha, o'zingiz uchun biror-bir izoh/eslatma yozib qo'yasizmi? ⬇️\n"
                "Agar xoxlamasangiz <b>Skip</b> deb yozib yuboring")
    elif lang == "uzk":
        text = ("Мижоз ҳақида, қўшимча, ўзингиз учун бирор-бир изоҳ/еслатма ёзиб қўясизми? ⬇️\n"
                "Агар хохламасангиз <b>Skip</b> деб ёзиб юборинг")
    elif lang == "rus":
        text = ("Хотели бы вы записать для себя дополнительные комментарии/заметки о клиенте? ⬇️\n"
                "Если вам это не нужно, просто скажите <b>Skip</b>.")
    await state.set_state(RentStatus.notes)
    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove()
    )
