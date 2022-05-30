from UserRepository import UserRepository
from UserService import UserService
from UserController import UserController
from WebDesktop import WebDesktop
from Validator import Validator
from Session import Session


def main():
    """
    Will instantiate the objects for the system
    """
    repository = UserRepository()
    validator = Validator(repository)
    session = Session(repository, validator)
    service = UserService(repository, validator)
    controller = UserController(service)
    web_desktop = WebDesktop(controller, session)

    web_desktop.execute()


if __name__ == '__main__':
    main()
