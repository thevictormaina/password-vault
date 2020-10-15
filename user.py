import string
import random

class User:
    """
    Class to define methods and properties of users
    """
    users = []

    def __init__(self, user_name, password, credentials=[]):
        """
        Define username and password properties
        """
        self.user_name = user_name
        self.password = password
        self.credentials = credentials
    
    def create_user(self):
        """
        Method to append new user to users list
        """
        User.users.append(self)
        
    def add_existing_credentials(self, credentials):
        """
        Method to add existing credentials to user account
        """
        self.credentials.append(credentials)

    def generate_new_password():
        password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=8))
        return password

    def add_new_credentials(self, credentials):
        """
        Method to create new credentials
        """
        creds = credentials
        if creds.password == "":
            creds.password = User.generate_new_password()
        else:
            pass

        self.credentials.append(credentials)

    def view_all_credentials(self):
        """
        Method to return a list of all credentials of a user
        """
        return self.credentials

    @classmethod
    def find_user(cls, user_name):
        """
        Search Users list for user using username
        """
        for user in cls.users:
            if user.user_name == user_name:
                return user
            else:
                pass
    
    @classmethod
    def user_index(cls, search_user):
        """
        Method to search Users list usinf user and return index
        """
        for user in User.users:
            if user == search_user:
                return User.users.index(user)
        return False
    
    @classmethod
    def list_users(cls):
        """
        Method to list usernames of all available users
        """

        user_names = []
        for user in User.users:
            user_names.append(user.user_name)
        
        return user_names