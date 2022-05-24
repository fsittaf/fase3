import re
from User import User
from Role import Role
from UserRepository import UserRepository
from Session import Session
from Constants import PASSWORD_MINIMUM_LEN


class Validator:
    """
    Help class that validate if the data entered is meeting the requirements
    """

    def __init__(self, repository: UserRepository, session: Session) -> None:
        self._repository = repository
        self.session = session

    def validate(self, user: User):
        '''
        Validate if user data enteres is compliant
        :param user: User object
        '''
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

        elif self.is_passwd_valid(user.password):
            raise Exception('Password len must be at least 6')

    def is_age_valid(self, age: str) -> bool:
        '''
        Check if age entered is valid, it should be >=0 && <=150
        :param age: String User age
        :return: Boolean
        '''
        try:
            age_int = int(age)
            if age_int >= 0 and age_int <= 150:
                return True
            else:
                False
        except ValueError:
            return False

    def is_email_valid(self, email: str) -> bool:
        '''
        Validate if email entered has the correct format
        :param email: String User email
        :return: Boolean
        '''
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return bool(re.fullmatch(regex, email))

    def is_passwd_valid(self, password: str) -> bool:
        if len(password) < PASSWORD_MINIMUM_LEN:
            return False

    # deixar aqui ou no session?
    def validate_session(self):
        if not self.session._is_logged:
            print('You are not logged in')
            return
