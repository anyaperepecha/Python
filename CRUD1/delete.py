from read import all_users_info


def delete_user(email, user_emails, users_storage):
    if email in user_emails:
        user_emails.remove(email)
        users_storage.pop(email)
        print("user_emails = ", user_emails)
        print("users_storage = ", users_storage)
    else:
        print('User with this email does not exist.')
