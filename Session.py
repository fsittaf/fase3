from UserRepository import UserRepository
from Validator import Validator

# TODO: TESTAR e criar Validation
# Criar timer p sessão?


class Session:
    def __init__(self, repository: UserRepository, validator: Validator) -> None:
        self._repository = repository
        self._validator = validator
        self._session_user = None
        self._is_logged = False

    def login(self, email: str, password: str):
        default_user = self._repository._default_user
        if email == default_user.name and password == default_user.password:
            print('Logged in!')
            self._session_user = default_user
            self._is_logged = True
            return

        if self._validator.is_email_valid(email):
            user = self._repository.get_by_email(email)
            if user.password == password:
                self._session_user = user
                self._is_logged = True
                return

        print('User not found')
