from create import create_user
from read import user_info, all_users_info
from update import update
from delete import delete_user
from help import help_info

user_emails = []
users_storage = {}

while True:
    action = input("Please enter create, read (read_all or read_user), update, delete or help: ")
    if action == "create":
        print('action = ', action)
        email = input("email: ")
        name = input("name: ")
        password = input("password: ")
        phone = input("phone: ")
        create_user(email,
                    name,
                    password,
                    phone,
                    user_emails,
                    users_storage)

        print("user_emails = ", user_emails)
        print("users_storage = ", users_storage)

    elif action == "read_all":
        print('action = ', action)
        all_users_info(users_storage)

    elif action == "read_user":
        print('action = ', action)
        email = input("Enter user email: ")
        user_info(email, user_emails, users_storage)

    elif action == "update":
        print('action = ', action)
        email = input('Enter your email: ')
        update(email, user_emails, users_storage)

    elif action == "delete":
        print('action = ', action)
        email = input('Enter your email: ')
        delete_user(email, user_emails, users_storage)

    elif action == "help":
        print('action = ', action)
        help_info()


