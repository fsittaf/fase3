from curses.ascii import isdigit
from User import User
from Role import Role
from EmailUtils import is_email_valid
from UserRepository import UserRepository


class Validator:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def validate(self, user: User):
        if user.name == '':
            raise Exception('Name cannot be empty')
        elif user.last_name == '':
            raise Exception('Last Name cannot be empty')
        elif not is_email_valid(user.email):
            raise Exception('Invalid email')
        # aqui
        elif not self.is_age_valid(user.age):
            raise Exception('Invalid age')
        elif user.role not in Role._member_names_:
            raise Exception('Invalid role')

    # Se eu tivesse colocado esse no método validade acima,
    # daria erro pq ao criar nao precisa passar id
    def is_id_valid(self, id):
        if id not in self.repository._users:
            raise Exception('ID not found')

    def is_age_valid(self, age: str) -> bool:
        try:
            age_int = int(age)
            if age_int >= 0 and age_int <= 150:
                return True
            else:
                False
        except ValueError:
            return False
