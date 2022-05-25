from UserRepository import UserRepository
from User import User
from Validator import Validator
# service


class UserService:
    """
        Service that manage the operations that a user can perform
    """

    def __init__(self, repository: UserRepository, validator: Validator):
        self.repository = repository
        self.validator = validator

    def get(self, id) -> User:
        return self.repository.get(id)

    def get_by_email(self, email) -> User:
        return self.repository.get_by_email(email)

    def get_all(self) -> list:
        return self.repository.get_all()

    def add(self, user: User, session_user) -> None:
        self.validator.validate(user, session_user)
        self.repository.add(user)

    # Validar permissão
    def update(self, old_user: User, new_user: User, session_user) -> None:
        self.repository.update(old_user, new_user, session_user)

    # Validar permissão
    def delete(self, id, session_user) -> None:
        self.validator.check_permissions(session_user, self.get(id))
        self.repository.delete(id, session_user)

    def get_by_name(self, name):
        return next((user for user in self.repository.get_all() if user.name == name), None)

    def filter_by_age(self, age):
        return [user for user in self.repository.get_all() if user.age == age]
