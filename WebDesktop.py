from DateUtils import formated_actual_time
from IdUtils import generate_id
from UserController import UserController
from User import User
from MenuUtils import menu_opt, menu_txt


class WebDesktop:
    """
    The main interface  allowing the interaction with  the user.
    The current MVP use a CLI that simulates the input of a form.
    """

    def __init__(self, controller: UserController):
        self.controller = controller

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

    def add(self, name, last_name, email, age, role):
        """
        Create a new User object
        """
        user = User(
            generate_id(), name, last_name, email, age, role, formated_actual_time()
        )
        # Talvez englobar um try/except em um fluxo maior?
        try:
            self.controller.add(user)
            print("User added successfully")
        except Exception as e:
            print("Error:", e)
            return

    def update(self, id, name, last_name, email, age, role):
        """
        Modfy the data of a user record
        """
        old_user = self.controller.get(id)
        if old_user is None:
            return
        user = User(
            id,
            name,
            last_name,
            email,
            age,
            role,
            old_user.created_at,
            formated_actual_time(),
        )
        self.controller.update(old_user, user)
        print("User updated successfully")

    def delete(self, id):
        """'
        Remove the user record from DB collections
        """
        try:
            self.controller.delete(id)
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
        """'
        Filter the list of users by age attribute
        """
        users = self.controller.filter_by_age(age)
        for user in users:
            print(user)

    # 'Menu e Dashboard' -> no futuro extrair para frontend do django

    def execute(self):
        """'
        Runs the menu options of the system
        """
        stop = False
        while not stop:
            print(menu_txt)
            choice = input("Enter your choice: ")
            print()

            if choice not in menu_opt:
                print("")

            elif choice == "1":
                self.get_all()

            elif choice == "2":
                input_id = input("Insira o ID: ")
                self.get(input_id)

            elif choice == "3":
                input_email = input("Insira o e-mail: ")
                self.get_by_email(input_email)

            elif choice == "4":
                print("Insira os dados")
                name = input("Nome: ")
                last_name = input("Último nome: ")
                email = input("Email: ")
                age = input("Idade: ")
                role = input("Role: ")
                self.add(name, last_name, email, age, role)

            elif choice == "5":
                print("Insira os dados")
                input_id = input("Insira o ID: ")
                name = input("Nome: ")
                last_name = input("Último nome: ")
                email = input("Email: ")
                age = input("Idade: ")
                role = input("Role: ")
                self.update(input_id, name, last_name, email, age, role)

            elif choice == "6":
                input_id = input("Insira o ID: ")
                self.delete(input_id)

            elif choice == "7":
                name = input("Nome: ")
                self.get_by_name(name)

            elif choice == "8":
                age = input("Idade: ")
                self.filter_by_age(age)

            elif choice == "9":
                print("Finalizando...")
                stop = True
