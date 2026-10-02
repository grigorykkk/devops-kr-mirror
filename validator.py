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

