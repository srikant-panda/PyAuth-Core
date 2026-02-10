import json,os


class Database:
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
            return 'User loggedin!'
        return 'Invalid Credential!'