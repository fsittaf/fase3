from User import User
from Role import Role
from EmailUtils import is_valid


class Validator:
    def __init__(self) -> None:
        pass

    def validate(self, user: User):
        if user.name == '':
            raise Exception('Name cannot be empty')
        elif user.last_name == '':
            raise Exception('Last Name cannot be empty')
        elif not is_valid(user.email):
            raise Exception('Invalid email')
        elif int(user.age) < 0 or int(user.age) > 150:
            raise Exception('Invalid age')
        elif user.role not in Role._member_names_:
            raise Exception('Invalid role')
