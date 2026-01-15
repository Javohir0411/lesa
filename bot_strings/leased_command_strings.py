class Leased:
    NOT_PRODUCT_IN_RENT = {
        "uzl": "📦 Hozircha ijaraga berilgan mahsulotlar yo'q",
        "uzk": "📦 Ҳозирча ижарага берилган маҳсулотлар йўқ",
        "rus": "📦 Товаров для аренды пока нет",
    }

    RESULT = {
        "uzl": "\n    🔢Miqdor: {rent.quantity}"
               "\n    👤Ijarachi: {renter.renter_fullname}"
               "\n    📞Tel: {renter.renter_phone_number}"
               "\n    📅{start_date} → {end_date}"
               "\n    💳To'lov: {rent.status.value}\n\n",

        "uzk": "\n    🔢Миқдор: {rent.quantity}"
               "\n    👤Ижарачи: {renter.renter_fullname}"
               "\n    📞Тел: {renter.renter_phone_number}"
               "\n    📅{start_date} → {end_date}"
               "\n    💳Тўлов: {rent.status.value}\n\n\n",

        "rus": "\n    🔢 Количество: {rent.quantity}"
               "\n    👤 Арендатор: {renter.renter_fullname}"
               "\n    📞 Телефон: {renter.renter_phone_number}"
               "\n    📅 {start_date} → {end_date}"
               "\n    💳 Оплата: {rent.status.value}\n\n"
    }
