import json
import sys

from DateUtils import get_current_time
from IdUtils import generate_id
from MenuUtils import menu_opt_admin, menu_opt_user, menu_txt_admin, menu_txt_user
from PasswUtils import generate_temp_passwd
from Session import Session
from User import Admin, User
from UserController import UserController


class WebDesktop:
    """
    The main interface  allowing the interaction with  the user.
    The current MVP use a CLI that simulates the input of a form.
    """

    def __init__(self, controller: UserController, session: Session):
        self.controller = controller
        self.session = session
        self.login()
        self.loadTestData()  # For demonstration

    # Deixar esse método aqui ou jogar p dentro do session?
    def login(self):
        while not self.session._is_logged:
            email = input("Email: ")
            password = input("Senha: ")
            self.session.login(email, password)

    def get_all(self):
        """
        Get all data
        """
        users = self.controller.get_all()
        for u in users:
            print(u)

    def get(self, id: str):
        """
        Get an especific user
        """
        user = self.controller.get(id)
        if user is None:
            print("User not found")
        else:
            print(user)

    def get_by_email(self, email: str):
        """'
        Get a user searching by e-mail field
        """
        user = self.controller.get_by_email(email)
        if user is None:
            print("User not found")
        else:
            print(user)

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

    def update(
        self,
        id,
        name,
        last_name,
        email,
        passwd,
        age,
        role,
        user_data=None,
        session_user=None,
    ):
        """
        Modfy the data of a user record
        """
        old_user = self.controller.get(id)
        if old_user is None:
            return

        old_user.name = name
        old_user.last_name = last_name
        old_user.email = email
        old_user.passwd = passwd
        old_user.age = age
        old_user.role = role
        old_user.updated_at = get_current_time()

        if old_user.role == "user":
            old_user.user_data = user_data

        self.controller.update(old_user, session_user)
        print("User updated successfully")

    def delete(self, id):
        """'
        Remove the user record from DB collections
        """
        try:
            self.controller.delete(id, self.session._session_user)
            print("User deleted successfully")
        except Exception as e:
            print(e)

    def get_by_name(self, name):
        """
        Get the user by the name field
        """
        user = self.controller.get_by_name(name)
        if user is None:
            print("User not found")
        else:
            print(user)

    def filter_by_age(self, age):
        """
        Filter the list of users by age attribute
        """
        users = self.controller.filter_by_age(age)
        for user in users:
            print(user)

    def get_user_data(self, id: str):
        """
        Get an especific user
        """
        user = self.controller.get(id)
        if user is None:
            print("User not found")
        else:
            print(user.user_data)

    # 'Menu e Dashboard' -> no futuro extrair para frontend do django

    def execute(self):
        """
        Runs the menu options of the system
        """
        stop = False
        while not stop and self.session._is_logged:
            # print(f"logged as {self.session._repository._users}")
            user_logged = self.session.get_user_from_session()
            print(
                "\n*******************************************************************************************"
            )
            print(f"\t\t\tUSER LOGGED IN as ({user_logged.role}) ")
            print(
                f"ID: {user_logged.user_id}  Name: {user_logged.name}  E-mail: {user_logged.email}"
            )
            print(
                "*******************************************************************************************"
            )
            # Menu Admin
            self.show_menu(user_logged.role)

    def show_menu(self, role):
        """
        Function to show the menu options according to the user role [admin, user]
        """
        if role == "admin":
            print(menu_txt_admin)
            choice = input("Enter your choice: ")
            print()

            if choice not in menu_opt_admin:
                print("")

            elif choice == "1":
                # Get all persons
                self.get_all()

            elif choice == "2":
                #  Get person by id
                input_id = input("Insira o ID: ")
                self.get(input_id)

            elif choice == "3":
                # Get person by email
                input_email = input("Insira o e-mail: ")
                self.get_by_email(input_email)

            elif choice == "4":
                #  Add person
                print("Insira os dados")
                user_data = None
                name = input("Nome: ")
                last_name = input("Último nome: ")
                email = input("Email: ")
                passwd = generate_temp_passwd()
                age = input("Idade: ")
                role = input("Role: ")
                if role == "user":
                    user_data = input("User data: ")
                self.add(name, last_name, email, passwd, age, role, user_data)

            elif choice == "5":
                # Update person
                print("Insira os dados")
                input_id = input("Insira o ID: ")
                name = input("Nome: ")
                last_name = input("Último nome: ")
                email = input("Email: ")
                passwd = input("Senha: ")
                age = input("Idade: ")
                role = input("Role: ")
                self.update(input_id, name, last_name, email, passwd, age, role)

            elif choice == "6":
                # Delete person
                input_id = input("Insira o ID: ")
                self.delete(input_id)

            elif choice == "7":
                # Get person by name
                name = input("Nome: ")
                self.get_by_name(name)

            elif choice == "8":
                # Filter person by age
                age = input("Idade: ")
                self.filter_by_age(age)

            elif choice == "9":
                # Logout
                self.session.logout()
                self.login()

            elif choice == "0":
                # Exit from system
                print("Finalizando...")
                # stop = True
                sys.exit()

        elif role == "user":

            print(menu_txt_user)
            choice = input("Enter your choice: ")
            print()

            user_logged = self.session.get_user_from_session()

            if choice not in menu_opt_user:
                print("")

            elif choice == "1":
                # Get person user
                self.get(
                    user_logged.user_id
                )  # Getting the person using the user_id from the current session
            elif choice == "2":
                # Print user data
                self.get_user_data(user_logged.user_id)

            elif choice == "3":
                # Update user data
                print("Insira os dados")
                # input_id = input(user_logged.user_id)
                new_user_data = input("User data: ")
                self.update(
                    id=user_logged.user_id,
                    name=user_logged.name,
                    last_name=user_logged.last_name,
                    email=user_logged.email,
                    passwd=user_logged.password,
                    age=user_logged.age,
                    role=user_logged.role,
                    user_data=new_user_data,
                )

            elif choice == "4":
                # logoutz
                self.session.logout()
                self.login()

            elif choice == "0":
                # Exit from system
                print("Finalizando...")
                # stop = True
                sys.exit()

    def loadTestData(self):
        """
        Loading the JSON file with some entities for demonstration
        """
        users_file = open("artifacts/users_data.json", "r")
        data_users = json.load(users_file)

        for user in data_users:
            role = user["role"]
            if role == "admin":
                # create Admin users
                print("Admin")
                self.add(
                    user["name"],
                    user["last_name"],
                    user["email"],
                    user["password"],
                    user["age"],
                    user["role"],
                )

            elif role == "user":
                # create User user
                self.add(
                    user["name"],
                    user["last_name"],
                    user["email"],
                    user["password"],
                    user["age"],
                    user["role"],
                    user["user_data"],
                )
