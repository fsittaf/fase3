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
        print(f"default: {self._repository._default_user}")
        default_user = self._repository._default_user
        if email == default_user.email and password == default_user.password:
            self._login_logout("Logged in!", default_user, True)
            return

        if self._validator.is_email_valid(email) and self._repository.get_by_email(
            email
        ):
            # user = self._repository.get_by_email(email)
            print(f"user: {user.email} - {user.password}")
            if user.password == password:
                self._login_logout("Logged in!", user, True)
                return

        print("User not found")

    def logout(self):
        self._login_logout("Logout!", None, False)

    # Testando esse método
    def _login_logout(self, arg0, arg1, arg2):
        print(arg0)
        self._session_user = arg1
        self._is_logged = arg2
