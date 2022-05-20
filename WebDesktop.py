from DateUtils import formated_actual_time
from IdUtils import generate_id
from UserController import UserController
from User import User
from MenuUtils import menu_opt, menu_txt


class WebDesktop:
    def __init__(self, controller: UserController):
        self.controller = controller

    def get_all(self):
        users = self.controller.get_all()
        for u in users:
            # TODO: colocar os outros attr
            print(f'ID: {u.user_id} - Full Name: {u.name} {u.last_name}')

    def get(self, id: str):
        user = self.controller.get(id)
        if user is None:
            print("User not found")
        else:
            print(user)

    def add(self, name, last_name, email, age, role):
        user = User(generate_id(), name, last_name, email,
                    age, role, formated_actual_time())
        try:
            self.controller.add(user)
            print('User added successfully')
        except Exception as e:
            print(e)

    # TODO:
    # Talvez refatorar esse update
    def update(self, id, name, last_name, email, age, role):
        user = User(id, name, last_name, email, age, role,
                    updated_at=formated_actual_time())
        self.controller.update(self.controller.get(id), user)
        print('User updated successfully')

    def delete(self, id):
        self.controller.delete(id)
        print('User deleted successfully')

    def get_by_name(self, name):
        user = self.controller.get_by_name(name)
        if user is None:
            print('User not found')
        else:
            print(user)

    def filter_by_age(self, age):
        users = self.controller.filter_by_age(age)
        for user in users:
            print(user)

    # 'Menu e Dashboard' -> no futuro extrair para frontend do django

    def execute(self):
        stop = False
        while not stop:
            print(menu_txt)
            choice = input('Enter your choice: ')
            print()

            if choice not in menu_opt:
                print('')

            elif choice == '1':
                self.get_all()

            elif choice == '2':
                input_id = input('Insira o ID: ')
                self.get(input_id)

            elif choice == '3':
                print('Insira os dados')
                name = input('Nome: ')
                last_name = input('Último nome: ')
                email = input('Email: ')
                age = input('Idade: ')
                role = input('Role: ')
                self.add(name, last_name, email, age, role)

            elif choice == '4':
                print('Insira os dados')
                input_id = input('Insira o ID: ')
                name = input('Nome: ')
                last_name = input('Último nome: ')
                email = input('Email: ')
                age = input('Idade: ')
                role = input('Role: ')
                self.update(input_id, name, last_name, email, age, role)

            elif choice == '5':
                input_id = input('Insira o ID: ')
                self.delete(input_id)

            elif choice == '6':
                name = input('Nome: ')
                self.get_by_name(name)

            elif choice == '7':
                age = input('Idade: ')
                self.filter_by_age(age)

            elif choice == '8':
                print('Finalizando...')
                stop = True
