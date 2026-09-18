"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.user import User
from controllers.user_controller import UserController

class UserView:
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
    def show_users(users):
        """ List users """
        print("\n".join(f"{user.id}: {user.name} ({user.email})" for user in users))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a new user """
        name = input("Nom d'utilisateur : ").strip()
        email = input("Adresse courriel : ").strip()
        return name, email