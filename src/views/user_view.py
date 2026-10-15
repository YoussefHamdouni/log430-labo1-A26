"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.user import User
from controllers.user_controller import UserController

class UserView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """
        while True:
            print("\n1. Montrer la liste d'utilisateurs\n2. Ajouter un utilisateur\n3. Supprimer un utilisateur\n4. Retour au menu principal")
            choice = input("Choisissez une option: ")
            if choice == '1':
                UserView.display_list()
            elif choice == '2':
                UserView.add()
            elif choice == '3':
                UserView.delete()
            elif choice == '4':
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def display_list():
        """ Show the list of users """
        controller = UserController()
        UserView.show_users(controller.list_users())
        controller.shutdown()

    @staticmethod
    def add():
        """ Fill the form and add a new user """
        name, email = UserView.get_inputs()
        controller = UserController()
        controller.create_user(User(None, name, email))
        controller.shutdown()

    @staticmethod
    def delete():
        """ Delete user with given ID """
        user_id = input("ID de l'utilisateur à supprimer : ").strip()
        controller = UserController()
        controller.delete_user(user_id)
        controller.shutdown()

    @staticmethod
    def show_users(users):
        """ List users """
        print("\n".join(f"{user.id}: {user.name} ({user.email})" for user in users))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a new user """
        name = input("Nom d'utilisateur : ").strip()
        email = input("Adresse courriel : ").strip()
        return name, email