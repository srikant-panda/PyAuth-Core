from User_Resitration_and_login.UserRegistration import UserAuthontication
from User_Resitration_and_login.Database import Database

print('__________Authontication___________')

choice= input('choose login or Registration : ')


if choice == 'register':
    user1 = UserAuthontication()
    user1.registration()
    
    status= Database.register(user1.username,user1.password)
    print(status)

    print(Database.user)
elif choice == 'login':
    Success = False
    while Success == False:
        user1 = UserAuthontication()
        user1.login()
        status = Database.login(user1.username,user1.password)
        print(status)
        if status == 'User loggedin!':
            Success = True

    if status == 'User loggedin!':
        choose = input('type change password to change the password or log out to exit: ')

        if choose == 'change password':
            old_password = input('Enter the old password')
            user1.change_password()
            status = Database.change_password(user1.username,old_password,user1.password)
            print(status)