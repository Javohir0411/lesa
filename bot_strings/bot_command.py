from aiogram.types import BotCommand
from utils.enums import LanguageEnum

class BotCommands:
    COMMANDS = {
        LanguageEnum.uzl.name: [
            BotCommand(command="start", description="Botni ishga tushirish"),
            BotCommand(command="help", description="Yordam olish"),
            BotCommand(command="rent", description="Ijaraga berishni boshlash")
        ],
        LanguageEnum.uzk.name: [
            BotCommand(command="start", description="Ботни ишга тушириш"),
            BotCommand(command="help", description="Ёрдам олиш"),
            BotCommand(command="rent", description="Ижарага бериш жараёнини бошлаш")
        ],
        LanguageEnum.rus.name: [
            BotCommand(command="start", description="Запустить бота"),
            BotCommand(command="help", description="Получить помощь"),
            BotCommand(command="rent", description="Начать процесс аренды")
        ],
    }