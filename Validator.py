import re
from User import User
from Role import Role
from UserRepository import UserRepository


class Validator:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def validate(self, user: User):
        if user.name == '':
            raise Exception('Name cannot be empty')
        elif user.last_name == '':
            raise Exception('Last Name cannot be empty')
        elif not self.is_email_valid(user.email):
            raise Exception('Invalid email')
        elif not self.is_age_valid(user.age):
            raise Exception('Invalid age')
        elif user.role not in Role._member_names_:
            raise Exception('Invalid role')

    def is_age_valid(self, age: str) -> bool:
        try:
            age_int = int(age)
            if age_int >= 0 and age_int <= 150:
                return True
            else:
                False
        except ValueError:
            return False

    def is_email_valid(self, email) -> bool:
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return bool(re.fullmatch(regex, email))
