from UserService import UserService


class UserController:
    def __init__(self, service: UserService) -> None:
        """
        Construct the controller for the User entity
        """
        self.service = service

    def get(self, id):
        """
        Return a user by ID passed in
        """
        return self.service.get(id)

    def get_by_email(self, email):
        """
        Return a user by e-mail passed in.
        """
        return self.service.get_by_email(email)

    def get_all(self):
        """
        Return the list of users in the collection
        """
        return self.service.get_all()

    def add(self, user):
        """
        Call to the UserService::add
        """
        self.service.add(user)

    def update(self, old_user, new_user):
        """
        Call to the UserService::update
        """
        self.service.update(old_user, new_user)

    def delete(self, id):
        """
        Call to the UserService::delete passing in the ID
        """
        self.service.delete(id)

    def get_by_name(self, name):
        """ 
        Return the user by name passed in.
        """
        return self.service.get_by_name(name)

    def filter_by_age(self, age):
        """ 
        Return a list of users that match the filter criteria
        """
        return self.service.filter_by_age(age)
