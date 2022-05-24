from UserRepository import UserRepository

# TODO: TESTAR e criar Validation
# Criar timer p sessão?


class Session:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository
        self._is_logged = False

    def login(self, email: str, password: str):
        default_user = self._repository._default_user
        if email == default_user.name and password == default_user.password:
            print('Logged in!')
            self._is_logged = True
            return default_user

        user = self._repository.get_by_email(email)
        if user.password == password:
            self._is_logged = True
            return user

        print('User not found')
