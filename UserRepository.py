# Repository

# Talvez usar um json p salvar temporariamente?
# Colocar User no init do repository?
class UserRepository:
    def __init__(self) -> None:
        self._users = []

    def add(self, user) -> None:
        self._users.append(user)

    def get(self, id):
        return next((user for user in self._users if user.user_id == id), None)

    def get_all(self) -> list:
        return self._users

    def update(self, old_user, new_user) -> None:
        self.delete(old_user.user_id)
        self.add(new_user)
        raise Exception("User not found.")

    def delete(self, id):
        for user in self._users:
            if user.user_id == id:
                self._users.remove(user)
                return
        raise Exception("User not found.")
