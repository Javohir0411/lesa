from enum import StrEnum


class LanguageEnum(StrEnum):
    uzl = "O'zbek tili (lotin)"
    uzk = "Ўзбек тили (крилл)"
    rus = "Русский язык"


class ProductTypeEnum(StrEnum):
    lesa = "Леса"
    monolit = "Монолит устун"
    taxta = "Тахта"


class LesaSizeEnum(StrEnum):
    katta = "katta"
    orta = "orta"
    kichik = "kichik"


class RentStatusEnum(StrEnum):
    active = "Ижарада"
    returned = "Қайтарилган"


class PaymentStatusEnum(StrEnum):
    full_paid = "Тўлиқ ✅"
    part_paid = "Қисман ⚠️"
    not_paid = "Тўланмаган ❌"


class LocationTypeEnum(StrEnum):
    map = "Харита",
    text = "Матн"


"""
CREATE TYPE ProductTypeEnum AS ENUM ('lesa', 'monolit', 'taxta');
CREATE TYPE LesaSizeEnum AS ENUM ('katta', 'orta', 'kichik', 'none');
CREATE TYPE RentStatusEnum AS ENUM ('full_paid', 'part_paid', 'not_paid');
CREATE TYPE LanguageEnum AS ENUM ('uzl', 'uzk', 'rus');
"""
