import json,os


class UserDatabase:
    file_path='User_Resitration_and_login/user.json'
    if os.path.exists(file_path):
        with open(file_path,'r') as f:
            user = json.load(f)
    else:
        user = {}
    @classmethod
    def register(cls,username,password):
        if username in cls.user:
            return 'username already registred.'
        # Add to memory
        cls.user[username] = password
        # Save to hard drive (the .json file)
        with open(cls.file_path,'w') as f:
            json.dump(cls.user,f)

        return 'user registered 😎.'
    @classmethod
    def change_password(cls,username,old_password,new_password):
        if username in cls.user:
            if old_password == new_password:
                return 'Error: new password can\'t be same as old password.'
            if cls.user[username] == old_password:
                cls.user[username] = new_password 
                with open(cls.file_path,'w') as f:
                    json.dump(cls.user,f)
                return 'Password changed successfully.'
            return 'Invalid credentials!'
        # return 'Invalid'
    @classmethod
    def login(cls,username,password):
        if username in cls.user and cls.user[username] == password:
            print('User loggedin!')
            return True
        print('Invalid Credential!')
    
                    
class AdminDatabase(UserDatabase):
    success = True
    file_path = 'User_Resitration_and_login/admin.json'

    if os.path.exists(file_path):
        with open(file_path,'r') as f:
            admin = json.load(f)
    else:
        admin = {}

    @classmethod
    def registration(cls,username,password,role):
        #check the request is worthy or not
        if role == 'Admin':
            #check database is empty or not
            if len(cls.admin) == 0:
                cls.admin[username] = password
                with open(cls.file_path,'w') as f:
                    json.dump(cls.admin,f)
                return 'Welcome Admin Dashboard!.With great power comes with great responsibility! Handle with care.'
            return 'Error: No more admin registration avilable. Contact the admin for this.'
        return 'Error: 403 Forbidden: You are not authorized.'
    @classmethod
    def login(cls,username,password,role):
        # check the request is worthy or not
        if role == 'Admin':
            # Check username is avilable or not
            if username in cls.admin:
                if password == cls.admin[username]:
                    # cls.success = True
                    return 'logged in | Welcome Admin Dashboard!.With great power comes with great responsibility! Handle with care.'
                return '!!!!_____Invalid Credentials_____!!!! 🧐 Who are you.'
            return 'There is no user like this.🤔'
        return 'Error: 403 Forbidden : You are not authorized . 😡 Who are you!'
    @classmethod
    def delete_user(cls,username,role):
        if role == 'Admin':
            if username in cls.user:
                del cls.user[username]
                with open(UserDatabase.file_path,'w') as f:
                    json.dump(cls.user,f)
                return 'User deleted'
            return 'Error: Usename not found'
        return '403 Forbidden: You are not authorized for this. 😡 Who are you!'