# from dataclasses import dataclass


# @dataclass(kw_only=True)
# class Parent:
#     name: str
#     age: int
#     ugly: bool = False
#     test_attr: str = "hello"


# @dataclass(kw_only=True)
# class Child(Parent):
#     school: str


# ch = Child(name="Kevin", age=17, school="42")
# print(ch.ugly, ch.test_attr)
# print(ch)


# FILES
import json

from DateUtils import get_current_time
from IdUtils import generate_id
from User import Admin, User
from UserController import UserController


class WebDesktopTest:
    def __init__(self, controller: UserController):
        self.controller = controller
        self.loadTestData()
        self.get_all()


def add(self, name, last_name, email, password, age, role, user_data=None):
    """
    Create a new User object
    """

    if role == "user":
        new_user = User(
            user_id=generate_id(),
            name=name,
            last_name=last_name,
            email=email,
            age=age,
            role=role,
            password=password,
            user_data=user_data,
            created_at=get_current_time(),
        )
    elif role == "admin":
        new_user = Admin(
            user_id=generate_id(),  # generated automatically
            name=name,
            last_name=last_name,
            email=email,
            age=age,
            role=role,
            password=password,
            created_at=get_current_time(),
        )
    # Talvez englobar um try/except em um fluxo maior?
    print(f"user: {new_user}")
    try:
        self.controller.add(new_user, self.session._session_user)
        print("User added successfully")
    except Exception as e:
        print("Error:", e)
        return


def get_all(self):
    """
    Get all data
    """
    users = self.controller.get_all()
    for u in users:
        print(u)


def loadTestData():
    """
    Loading the JSON file with some entities
    """
    users_file = open("artifacts/users_data.json", "r")
    data_users = json.load(users_file)

    for user in data_users:
        role = user["role"]
        if role == "admin":
            # create admin users
            print("Admin")
            add(
                user["name"],
                user["last_name"],
                user["email"],
                user["password"],
                user["age"],
                user["role"],
            )

        elif role == "user":
            # cretae User user
            print("User")
            add(
                user["name"],
                user["last_name"],
                user["email"],
                user["password"],
                user["age"],
                user["role"],
                user["user_data"],
            )
