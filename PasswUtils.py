# Will be used for the generation of the password when user is created
# Or when the reset password is hit
# if email and passwd are valids successful login
import secrets
import string


def generate_temp_passwd(length):
    return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
