# import logging
#
# from aiogram import Router, F, types
# from aiogram.fsm.context import FSMContext
#
# from bot_strings.rent_command_strings import RentStrings
# from database.session import get_user_language
# # from keyboards.common_keyboards import build_location_type_kb
# from states import RentStatus
# # from utils.enums import LocationTypeEnum
#
# router = Router(name=__name__)
#
#
# @router.message(F.text, RentStatus.location_type)
# async def handle_location_type_message(message: types.Message, state: FSMContext):
#     location_type = message.text
#     await state.update_data(location_type=location_type)
#     data = await state.get_data()
#     logging.info(f"DATA-NI MA'LUMOTLARI: {data}")
#     await state.set_state(RentStatus.location_request)
#     lang = await get_user_language(message)
#     text = RentStrings.LOCATION_REQUEST[lang]
#     await message.answer(
#         text=text,
#         reply_markup=types.ReplyKeyboardRemove()
#     )

# # LocationTypeEnum.text.name

# @router.message(F.text, RentStatus.location_type)
# async def handle_location_type_message(message: types.Message, state: FSMContext):
#     location_type = message.text
#     await state.update_data(location_type=location_type)
#
#     # Tilni olish
#     lang = await get_user_language(message)
#
#     # Tugma qiymatlarini tekshirish
#     map_text = RentStrings.LOCATION_KB_TRANSLATION[lang][LocationTypeEnum.map.name]
#     text_text = RentStrings.LOCATION_KB_TRANSLATION[lang][LocationTypeEnum.text.name]
#
#     if location_type == map_text:
#         # Xarita tanlandi
#         await state.set_state(RentStatus.location_request)
#         reply_text = RentStrings.LOCATION_REQUEST[lang]
#     elif location_type == text_text:
#         # Matn tanlandi
#         await state.set_state(RentStatus.location_text)
#         reply_text = RentStrings.LOCATION_TEXT_REQUEST[lang]  # matn uchun alohida so'rov
#     else:
#         # Noma'lum tugma, foydalanuvchini qayta so'rash
#         reply_text = RentStrings.LOCATION_INVALID[lang]
#         await message.reply(text=reply_text, reply_markup=build_location_type_kb[lang])
#         return
#
#     # Logging va javob
#     data = await state.get_data()
#     logging.info(f"DATA-NI MA'LUMOTLARI: {data}")
#
#     await message.answer(
#         text=reply_text,
#         reply_markup=types.ReplyKeyboardRemove()
#     )
