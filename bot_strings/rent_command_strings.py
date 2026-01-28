from utils.enums import LanguageEnum, ProductTypeEnum, LesaSizeEnum


class RentStrings:
    RENT_STARTING_PROCESS = {
        LanguageEnum.uzl.name:
            "Unday bo'lsa, ijaraga berish jarayonini boshlaymiz.\n"
            "Quyidan, ijaraga bermoqchi bo'lgan mahsulotingizni tanlang\n\n",

        LanguageEnum.uzk.name:
            "Ундай бўлса, ижарага бериш жараёнини бошлаймиз.\n"
            "Қуйидан, ижарага бермоқчи бўлган маҳсулотингизни танланг\n\n",

        LanguageEnum.rus.name:
            "Затем мы начнем процесс аренды.\n"
            "Ниже выберите товар, который хотите арендовать.\n\n"
    }

    CHOOSE_PRODUCT_KEYBOARD = {
        LanguageEnum.uzl.name: {
            ProductTypeEnum.lesa.name:
                "Lesa"
                # LesaSizeEnum.katta.name: "Lesa Katta",
                # LesaSizeEnum.orta.name: "Lesa O'rta",
                # LesaSizeEnum.kichik.name: "Lesa Kichik",
            ,

            ProductTypeEnum.monolit.name: "Monolit stoyka",
            ProductTypeEnum.taxta.name: "Taxta",
        },

        LanguageEnum.uzk.name: {
            ProductTypeEnum.lesa.name:
                "Леса"
                # LesaSizeEnum.katta.name: "Леса Катта",
                # LesaSizeEnum.orta.name: "Леса Ўрта",
                # LesaSizeEnum.kichik.name: "Леса Кичик",
            ,

            ProductTypeEnum.monolit.name: "Монолит стойка",
            ProductTypeEnum.taxta.name: "Тахта",
        },

        LanguageEnum.rus.name: {
            ProductTypeEnum.lesa.name:
                "Леса"
                # LesaSizeEnum.katta.name: "Большая Леса",
                # LesaSizeEnum.orta.name: "Средняя Леса",
                # LesaSizeEnum.kichik.name: "Маленькая Леса",
            ,

            ProductTypeEnum.monolit.name: "Монолитный стенд",
            ProductTypeEnum.taxta.name: "Доска",
        },
    }

    SELECT_INVALID_PRODUCT = {
        LanguageEnum.uzl.name: "Iltimos, quyidan kerakli mahsulotni birini tanlang!",
        LanguageEnum.uzk.name: "Илтимос, қуйидан керакли маҳсулотни бирини танланг!",
        LanguageEnum.rus.name: "Пожалуйста, выберите нужный вам товар ниже!",
    }

    INSERT_QUANTITY_PRODUCT = {
        LanguageEnum.uzl.name: "Kerakli miqdorni kiriting: ⬇️",
        LanguageEnum.uzk.name: "Керакли миқдорни киритинг: ⬇️",
        LanguageEnum.rus.name: "Введите необходимое количество: ⬇️",
    }

    LESA_SIZE_TRANSLATION = {
        "uzl": {
            LesaSizeEnum.katta.name: "Katta",
            LesaSizeEnum.orta.name: "O'rta",
            LesaSizeEnum.kichik.name: "Kichik",
        },
        "uzk": {
            LesaSizeEnum.katta.name: "Катта",
            LesaSizeEnum.orta.name: "Ўрта",
            LesaSizeEnum.kichik.name: "Кичик",
        },
        "rus": {
            LesaSizeEnum.katta.name: "Большой",
            LesaSizeEnum.orta.name: "Середина",
            LesaSizeEnum.kichik.name: "Маленький",
        }
    }

    INSERT_INVALID_SIZE = {
        "uzl": "Iltimos, quyidan kerakli hajmni tanlang!",
        "uzk": "Илтимос, қуйидан керакли ҳажмни танланг!",
        "rus": "Пожалуйста, выберите необходимый размер ниже!",
    }

    CHOOSE_ANOTHER_PRODUCT = {
        "uzl": "Yana qo'shmoqchi bo'lgan mahsulotingizni belgilang: \n\n",
        "uzk": "Яна қўшмоқчи бўлган маҳсулотингизни белгиланг: \n\n",
        "rus": "Выберите товар, который хотите добавить: \n\n",
    }

    YES_NO_TEXT = {
        "uzl": {"yes": "Ha", "no": "Yo‘q"},
        "uzk": {"yes": "Ха", "no": "Йўқ"},
        "rus": {"yes": "Да", "no": "Нет"},
    }

    ASK_RENTER_FULLNAME = {
        "uzl": "Yaxshi, endi navbatda, ijaraga oluvchining ism va familiyasini kiriting(masalan, Ali Valiyev): ",
        "uzk": "Яхши, энди навбатда, ижарага олувчининг исм ва фамилиясини киритинг(масалан, Али Валиев):",
        "rus": "Хорошо, теперь введите имя и фамилию арендатора (например, Али Валиев):",
    }

    INVALID_YES_NO = {
        "uzl": "Iltimos, javobingizni quyidagi tugmalar orqali bering⬇️",
        "uzk": "Илтимос, жавобингизни қуйидаги тугмалар орқали беринг⬇️",
        "rus": "Пожалуйста, ответьте, используя кнопки ниже⬇️",
    }

    GET_RENT_START_DATE = {
        "uzl": "Ijarani boshlanish sanasini kiriting <b>(DD.MM.YYYY)</b>: ",
        "uzk": "Ижарани бошланиш санасини киритинг <b>(ДД.ММ.ЙЙЙЙ)</b>: ",
        "rus": "Введите дату начала аренды <b>(ДД.ММ.ГГГГ)</b>:",
    }

    GET_RENT_END_DATE = {
        "uzl": "Ijarani tugash sanasini ham kiriting <b>(DD.MM.YYYY)</b>: ",
        "uzk": "Ижарани тугаш санасини ҳам киритинг <b>(ДД.ММ.ЙЙЙЙ)</b>: ",
        "rus": "Также укажите дату окончания аренды <b>(ДД.ММ.ГГГГ)</b>: ",
    }

    ASK_LOCATION_TYPE = {
        "uzl": "Joylashuvni qaysi ko'rinishda yuborasiz?",
        "uzk": "Жойлашувни қайси кўринишда юборасиз?",
        "rus": "В каком формате вы отправляете местоположение?",
    }

    LOCATION_INVALID = {
        "uzl": "Joylashuvni yuborish turini tugmalar orqali belgilang⬇️",
        "uzk": "Жойлашувни юбориш турини тугмалар орқали белгиланг⬇️",
        "rus": "Укажите тип отправки по местоположению с помощью кнопок.⬇️",
    }

    # LOCATION_KB_TRANSLATION = {
    #     "uzl": {
    #         LocationTypeEnum.map.name: "Xarita📍",
    #         LocationTypeEnum.text.name: "Matn📝",
    #     },
    #     "uzk": {
    #         LocationTypeEnum.map.name: "Харита📍",
    #         LocationTypeEnum.text.name: "Матн📝",
    #     },
    #     "rus": {
    #         LocationTypeEnum.map.name: "Карта📍",
    #         LocationTypeEnum.text.name: "Текст📝",
    #     },
    # }

    LOCATION_REQUEST = {
        "uzl": "Mijozning joylashuvini yuboring📍 ",
        "uzk": "Мижознинг жойлашувини юборинг📍 ",
        "rus": "Отправить местоположение клиента📍 ",
    }

    SENT_LOCATION_INFO = {
        "uzl":
            "📍<b>Lokatsiya qabul qilindi</b>\n\n"
            "<b>Latitude</b>: <u>{renter_latitude}</u>\n"
            "<b>Longitude</b>: <u>{renter_longitude}</u>\n"
            "<b>Masofa</b>: <u>{distance_km}</u> km\n\n"
            "<b>Yetkazib berish narxi</b>:\n"
            "<b>2.5 km radius uchun: </b>\n"
            "\n    <b>Yetkazib berish:</b> <u>30.000</u> so'm\n"
            "\n    <b>Qayta olib kelish:</b> <u>30.000</u> so'm\n"
            "\n    <b>Umumiy:</b> <u>60.000</u> so'm\n\n"
            "<b>Kiritilgan joylashuv uchun</b>: <u>{price_delivery}</u> so'm",

        "uzk":
            "<b>📍Локация қабул қилинди</b>\n\n"
            "<b>Латитуде</b>: <u>{renter_latitude}</u>\n"
            "<b>Лонгитуде</b>: <u>{renter_longitude}</u>\n"
            "<b>Масофа</b>: <u>{distance_km}</u> км\n\n"
            "<b>Етказиб бериш нархи</b>:\n"
            "<b>2.5 км радиус учун: </b>\n"
            "\n    <b>Етказиб бериш:</b> <u>30.000</u> сўм\n"
            "\n    <b>Қайта олиб келиш:</b> <u>30.000</u> сўм\n"
            "\n    <b>Умумий:</b> <u>60.000</u> сўм\n\n"
            "<b>Киритилган жойлашув учун</b>: <u>{price_delivery}</u> сўм",

        "rus":
            "📍<b>Принятое местоположение</b>\n\n"
            "<b>Широта</b>: <u>{renter_latitude}</u>\n"
            "<b>Долгота</b>: <u>{renter_longitude}</u>\n"
            "<b>Расстояние</b>: <u>{distance_km}</u> км\n\n"
            "<b>Стоимость доставки</b>:\n"
            "<b>В радиусе 2,5 км:</b>\n"
            "\n    <b>Доставка:</b> <u>30 000</u> сумов\n"
            "\n    <b>Возврат:</b> <u>30 000</u> сумов\n"
            "\n    <b>Итого:</b> <u>60 000</u> сумов\n\n"
            "<b>Для указанного местоположения:</b> <u>{price_delivery}</u> сум",
    }
