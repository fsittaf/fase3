import email

# Talvez usar um json p salvar temporariamente?
# Colocar User no init do repository?

# Repository


class UserRepository:
    def __init__(self) -> None:
        self._users = []

    def add(self, user) -> None:
        for u in self._users:
            if u.email == user.email:
                raise Exception("Email already in use")
        self._users.append(user)

    def get(self, id):
        return next((user for user in self._users if user.user_id == id), None)

    def get_all(self) -> list:
        if len(self._users) == 0:
            print('No users created')
        return self._users

    def update(self, old_user, new_user) -> None:
        self.delete(old_user.user_id)
        self.add(new_user)

    def delete(self, id):
        for user in self._users:
            if user.user_id == id:
                self._users.remove(user)
                return
        raise Exception("User not found.")
