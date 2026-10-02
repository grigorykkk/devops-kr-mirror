def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    import re
    pattern = r'^\+?7\d{10}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС (формат XXX-XXX-XXX YY)."""
    import re
    return bool(re.match(r'^\d{3}-\d{3}-\d{3} \d{2}$', snils))


# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

