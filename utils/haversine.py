from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    """
    Bu funksiya ikkita nuqta orasidagi masofani hisoblaydi.
    lat1, lon1 - birinchi nuqta (masalan, uy)
    lat2, lon2 - ikkinchi nuqta (masalan, maktab)
    Natija: masofa km da
    """

    # 1️⃣ Graduslarni radianlarga o'zgartiramiz
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Trigonometrik hisob-kitoblar radianlarda bo‘lishi kerak

    # 2️⃣ Farqni topamiz
    dlat = lat2 - lat1  # kenglik farqi
    dlon = lon2 - lon1  # uzunlik farqi

    # 3️⃣ Haversine formula
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    # Bu formula Yer sathidagi ikki nuqta orasidagi "burchak"ni beradi

    # 4️⃣ Burchakni masofaga aylantiramiz
    c = 2 * asin(sqrt(a))
    # sqrt(a) - yarim burchak, asin bilan to‘liq burchak c olinadi

    # 5️⃣ Yer radiusi (km da)
    r = 6371

    # 6️⃣ Masofani hisoblaymiz
    distance = c * r
    return distance
