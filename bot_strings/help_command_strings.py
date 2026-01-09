from utils.enums import LanguageEnum
from aiogram.utils import markdown

class HelpStrings:
    TEXT = {
        LanguageEnum.uzl.name: (
            "🤖 <b>Bot nima qiladi?</b>\n\n"
            "Bu bot sizga xizmatlar bilan tez va qulay ishlash imkonini beradi.\n\n"
            "<b>Mavjud buyruqlar:</b>\n"
            "/start — Botni ishga tushirish\n"
            "/help — Yordam va qo‘llanma\n"
            "/rent - Ijaraga berish jarayonini boshlash"
        ),

        LanguageEnum.uzk.name: (
            "🤖 <b>Бот нима қилади?</b>\n\n"
            "Бу бот сизга хизматлар билан тез ва қулай ишлаш имконини беради.\n\n"
            "<b>Мавжуд буйруқлар:</b>\n"
            "/start — Ботни ишга тушириш\n"
            "/help — Ёрдам ва қўлланма\n"
            "/rent - Ижарага бериш жараёнини бошлаш"
        ),

        LanguageEnum.rus.name: (
            "🤖 <b>Что делает бот?</b>\n\n"
            "Этот бот помогает вам быстро и удобно пользоваться сервисом.\n\n"
            "<b>Доступные команды:</b>\n"
            "/start — Запустить бота\n"
            "/help — Справка\n"
            "/rent - Начать процесс аренды"
        ),
    }