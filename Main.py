from wsgiref.validate import validator
from UserRepository import UserRepository
from UserService import UserService
from UserController import UserController
from WebDesktop import WebDesktop
from Validator import Validator


def main():
    repository = UserRepository()
    validator = Validator()
    service = UserService(repository, validator)
    controller = UserController(service)
    web_desktop = WebDesktop(controller)

    web_desktop.execute()


if __name__ == '__main__':
    main()
