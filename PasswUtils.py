# Will be used for the generation of the password when user is created
# Or when the reset password is hit
# if email and passwd are valids successful login
import random
import string
from Constants import PASSWORD_MINIMUM_LEN

# import secrets


# Teste


def random_len():
    return random.randint(2, PASSWORD_MINIMUM_LEN)


def generate_temp_passwd():
    letters_len = random_len()
    digits_len = PASSWORD_MINIMUM_LEN - letters_len

    letters = "".join((random.choice(string.ascii_letters) for _ in range(letters_len)))
    digits = "".join((random.choice(string.digits) for _ in range(digits_len)))

    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    # print(f"password generated: {''.join(sample_list)}")
    return "".join(sample_list)


# def generate_temp_passwd():
#     return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(PASSWORD_MINIMUM_LEN))
