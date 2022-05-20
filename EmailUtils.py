import re

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def is_email_valid(email) -> bool:
    return bool(re.fullmatch(regex, email))
