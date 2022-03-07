def user_message(email, users_storage):
    print("User_email: ", email, '\n',
          "User_name: ", users_storage[email]['name'], '\n',
          "User_password: ", users_storage[email]['password'], '\n',
          "User_phone: ", users_storage[email]['phone'])


def user_info(email, user_emails, users_storage):
    if email in user_emails:
        return user_message(email, users_storage)
    else:
        print("No user with email: ", email)


def all_users_info(users_storage):
    for k, v in users_storage.items():
        print("User_email: ", k, '\n',
              "User_name: ", v['name'], '\n',
              "User_password: ", v['password'], '\n',
              "User_phone: ", v['phone'])
