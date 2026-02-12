from User_Resitration_and_login.UserRegistration import UserAuthontication
from User_Resitration_and_login.Database import UserDatabase, AdminDatabase as AdminDB
from User_Resitration_and_login.Admin import AdminUser
print('__________Authontication___________')

choice= input('choose login or Register or admin panel: ')


if choice.lower() == 'register':
    user1 = UserAuthontication()
    user1.registration()
    
    status= UserDatabase.register(user1.username,user1.password)
    print(status)
elif choice.lower() == 'login':
    Success = False
    while True:
        user1 = UserAuthontication()
        user1.login()
        status = UserDatabase.login(user1.username,user1.password)
        if status == True:
            break
    if status == True:
        while True:
            choose = input('type change password to change the password or log out to exit: ')

            if choose == 'change password':
                # old_password = input('Enter the old password: ')
                user1.change_password()
                status = UserDatabase.change_password(user1.username,user1.old_password,user1.password)
                print(status)
            elif choose == 'log out':
                break
            else:
                print('Invalid action!')
elif choice.lower() == 'admin panel':
    choose = input('Register or login: ')

    if choose.lower() == 'register':
        admin1 = AdminUser()
        admin1._AdminUser__register()
        status=AdminDB.registration(admin1.username,admin1.password,admin1.role)
        print(status)
    elif choose.lower() == 'login':
        success = False
        while success == False:
            admin1 = AdminUser()
            admin1.login()
            status=AdminDB.login(admin1.username, admin1.password,admin1.role)
            print(status)
            if status == 'logged in | Welcome Admin Dashboard!.With great power comes with great responsibility! Handle with care.':
                success = True
        print('''Choose Activity:

        1.For list users tye list.
        2.For Delete a user type del.
        3.For exit type exit.
        ''')
        while  True:
            choose = input("Enter the activity to perform: ")
            if success == True:
                if choose.lower() == 'list':
                    users = list(UserDatabase.user)
                    print(users)
                    # break
                elif choose.lower() == 'del':
                    target_username= admin1.delete_user()
                    status= AdminDB.delete_user(target_username,admin1.role)
                    print(status)
                    # break
                elif choose.lower() == 'exit':
                    break
                else:
                    print('Invalid action!')
