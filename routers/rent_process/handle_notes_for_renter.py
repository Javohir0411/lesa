# import logging
#
# from aiogram import Router, F, types
# from aiogram.fsm.context import FSMContext
#
# from database.session import get_user_language
# from states import RentStatus
#
# router = Router(name=__name__)
#
#
# @router.message(F.text, RentStatus.notes)
# async def handle_notes_for_renter(message: types.Message, state: FSMContext):
#     text = message.text
#     lang = await get_user_language(message)
#     if text.casefold() == "skip":
#         if lang == "uzl":
#             rent_result = "Ijara ma'lumotlari saqlandi!✅"
#         elif lang == "uzk":
#             rent_result = "Ижара маълумотлари сақланди!✅"
#         elif lang == "rus":
#             rent_result = "Информация об аренде сохранена!✅"
#         await message.answer(
#             text=rent_result,
#             reply_markup=types.ReplyKeyboardRemove()
#         )
#     else:
#         await state.update_data(notes=text)
#         data = await state.get_data()
#         logging.info(f"IJARA MA'LUMOTLARI: {data}")
#         if lang == "uzl":
#             rent_result = "Ijara ma'lumotlari saqlandi!✅"
#         elif lang == "uzk":
#             rent_result = "Ижара маълумотлари сақланди!✅"
#         elif lang == "rus":
#             rent_result = "Информация об аренде сохранена!✅"
#         await message.answer(
#             text=rent_result,
#             reply_markup=types.ReplyKeyboardRemove()
#         )

import logging
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from database.session import async_session_maker  # AsyncSession yaratish uchun
from database.session import get_user_language
from states import RentStatus
from db.save_rents import save_rent_from_fsm  # Sizning saqlash funksiyangiz

router = Router(name=__name__)


@router.message(F.text, RentStatus.notes)
async def handle_notes_for_renter(message: types.Message, state: FSMContext):
    text = message.text
    lang = await get_user_language(message)

    # 1️⃣ FSMContext ga notes saqlash
    if text.casefold() != "skip":
        await state.update_data(notes=text)

    # 2️⃣ FSMContext dan barcha ma'lumotlarni olish
    data = await state.get_data()
    logging.info(f"IJARA MA'LUMOTLARI: {data}")

    # 3️⃣ Bazaga saqlash
    try:
        async with async_session_maker() as session:
            rents = await save_rent_from_fsm(data)  # Bu funksiya Renter va Rentlarni saqlaydi
    except Exception as e:
        logging.error(f"Rents saqlashda xatolik: {e}")
        error_msg = {
            "uzl": "Xatolik yuz berdi, ma'lumot saqlanmadi ❌",
            "uzk": "Хато юз берди, маълумот сақланмади ❌",
            "rus": "Произошла ошибка, данные не сохранены ❌"
        }
        await message.answer(text=error_msg.get(lang, "Xatolik ❌"))
        return

    # 4️⃣ Foydalanuvchiga batafsil xabar tayyorlash
    message_lines = []
    for rent in rents:
        product_name = f"{rent.product.product_type}"
        if rent.product.product_size:
            product_name += f" ({rent.product.product_size})"
        days = (rent.end_date - rent.start_date).days
        line = f"<b>{product_name}</b> — <u>{rent.quantity}</u> дона\n"
        line += f"<b>Ижара кунлари:</b> <u>{days}</u>\n"
        line += f"<b>Маҳсулот нархи:</b> <u>{rent.product_price}</u> сўм\n"
        line += f"<b>Етказиб бериш хизмати:</b> <u>{rent.delivery_price}</u> сўм\n"
        line += f"<b>Жами:</b> <u>{rent.rent_price}</u> сўм\n"
        message_lines.append(line)

    # 4️⃣ Foydalanuvchiga xabar
    header = {
        "uzl": "Ijara ma'lumotlari saqlandi!✅",
        "uzk": "Ижара маълумотлари сақланди!✅",
        "rus": "Информация об аренде сохранена!✅"
    }.get(lang, "Ижара маълумотлари сақланди!✅")

    final_text = header + "\n\n" + "\n".join(message_lines)

    await message.answer(
        text=final_text,
        reply_markup=types.ReplyKeyboardRemove()
    )

    # 5️⃣ FSMContext ni tozalash
    await state.clear()
