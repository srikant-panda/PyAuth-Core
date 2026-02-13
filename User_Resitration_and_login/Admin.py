from .UserRegistration import UserAuthontication

class AdminUser(UserAuthontication):
    def __init__(self):
        super().__init__()
    def __register(self):
        self.role = 'Admin'
        UserAuthontication.registration(self)
        return self.role
    def delete_user(self):
        target= input("enter the username to delete: ")
        self.role = 'Admin'
        return target
    def login(self):
        self.username = input('Enter the username: ')
        self.password = input('Enter the password: ')
        self.role = 'Admin'