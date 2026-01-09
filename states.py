from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()


class RentStatus(StatesGroup):
    product_choice = State()
    lese_size_choice = State()
    quantity = State()
    additional_choice = State()
    renter_fullname = State()
    renter_phone_number = State()
    renter_passport_info = State()
    start_date = State()
    end_date = State()
    location = State()
    delivery_needed = State()
    delivery_price = State()
    notes = State()
    confirm = State()
