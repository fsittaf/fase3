from UserRepository import UserRepository
from User import User
from Validator import Validator
# service


class UserService:
    def __init__(self, repository: UserRepository, validator: Validator):
        self.repository = repository
        self.validator = validator

    def get(self, id) -> User:
        return self.repository.get(id)

    def get_all(self) -> list:
        return self.repository.get_all()

    def add(self, user: User) -> None:
        self.validator.validate(user)
        self.repository.add(user)

    def update(self, old_user: User, new_user: User) -> None:
        self.validator.validate(new_user)
        self.repository.update(old_user, new_user)

    def delete(self, id) -> None:
        self.repository.delete(id)

    def get_by_name(self, name):
        return next((user for user in self.repository.get_all() if user.name == name), None)

    def filter_by_age(self, age):
        return [user for user in self.repository.get_all() if user.age == age]
