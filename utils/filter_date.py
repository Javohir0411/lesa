from datetime import datetime

def is_date(text: str) -> bool:
    try:
        datetime.strptime(text, "%d.%m.%Y")
        return True
    except ValueError:
        return False
