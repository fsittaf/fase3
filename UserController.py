from UserService import UserService


class UserController:
    def __init__(self, service: UserService) -> None:
        self.service = service

    def get(self, id):
        return self.service.get(id)

    def get_by_email(self, email):
        return self.service.get(email)

    def get_all(self):
        return self.service.get_all()

    def add(self, user):
        self.service.add(user)

    def update(self, old_user, new_user):
        self.service.update(old_user, new_user)

    def delete(self, id):
        self.service.delete(id)

    def get_by_name(self, name):
        return self.service.get_by_name(name)

    def filter_by_age(self, age):
        return self.service.filter_by_age(age)
