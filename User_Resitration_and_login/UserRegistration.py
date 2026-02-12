
class UserAuthontication:
    def __init__(self):
        self.username = None
        self.password = None
        # self.old_password = None
        self.is_valid = True
        self.has_upper = False
        self.has_smaller = False
        self.has_number = False
        self.has_specialcharacter= False
        self.successUsername = False
        self.successPassword = False
    def password_validator(self):
        while self.successPassword == False:
            self.is_valid=True
            self.has_upper = False
            self.has_smaller = False
            self.has_number = False
            self.has_specialcharacter= False
            self.successPassword = False
            self.password = input('Enter the password: ')
            
            if len(self.password) == 0:
                print('Error: password can\'t be empty.')
                # self.is_valid = False
                continue
            if ' ' in self.password:
                print('Error: pasword should not contain spaces.')
                # self.is_valid = False
                continue
            if (self.username.lower() in self.password.lower()):
                print('Error: password should not contain the username.')
                # self.is_valid = False
                continue
            if len(self.password)<8:
                print('Error: password should contain atleast 8 character.')
                # self.is_valid = False
                continue
            confirm_password: str = input('Re-enter the password to confirm: ')
            if self.password != confirm_password:
                print('Error: Password not match.')
                continue
            for i in self.password:
                if i.isupper():
                    self.has_upper = True
                if i.islower():
                    self.has_smaller = True
                if i.isdigit():
                    self.has_number =  True
                if not i.isalnum():
                    self.has_specialcharacter = True
            if not self.has_upper:
                print('Error: password should have atleast one uppercase.')
                self.is_valid = False
            if not self.has_smaller:
                print('Error: password should have atleast one lowercase.')
                self.is_valid = False
            if not self.has_number:
                print('Error: password should have atleast one number.')
                self.is_valid = False
            if not self.has_specialcharacter:
                print('Error: password should have atleast one specialcharacter.')
                self.is_valid = False 

            if self.is_valid == True:
                self.successPassword = True    


    def registration(self):
        while self.successUsername == False:
            self.username = input('Enter the username: ')
            if len(self.username) == 0:
                print('Error: username can\'t be empty.')
                continue
            elif ' ' in self.username:
                print('Error: username should not contaon space')
                continue
            else:
                self.successUsername = True
        self.password_validator()

    def login(self):
        self.username = input("Enter the username: ")
        self.password = input('Enter the password: ')

    def change_password(self):
        self.old_password = input('Enter the old password:')
        self.password_validator()