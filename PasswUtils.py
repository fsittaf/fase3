# no fluxo falamos que iriamos gerar uma senha aleatoria,
# mas isso só terá funcionalidade ao criar sessions
# if email and passwd are valids successful login
import secrets
import string


def generate_temp_passwd(length):
    return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))