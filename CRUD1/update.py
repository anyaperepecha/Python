from read import user_message


def update_email(email, user_emails, users_storage):
    new_email = input('Enter new email: ')
    for i in range(len(user_emails)):
        if user_emails[i] == email:
            user_emails[i] = new_email
            users_storage[new_email] = users_storage.pop(email)
            return user_message(new_email, users_storage)


def update_name(email, users_storage):
    new_name = input('Enter new name: ')
    users_storage[email]['name'] = new_name
    return user_message(email, users_storage)


def update_password(email, users_storage):
    new_password = input('Enter new password: ')
    users_storage[email]['password'] = new_password
    return user_message(email, users_storage)


def update_phone(email, users_storage):
    new_phone = input('Enter new phone: ')
    users_storage[email]['phone'] = new_phone
    return user_message(email, users_storage)


def update(email, user_emails, users_storage):
    if email in user_emails:
        parameter = input('Please, enter parameter to update: email, name, password, phone: ')
        if parameter == 'email':
            update_email(email, user_emails, users_storage)
        elif parameter == 'name':
            update_name(email, users_storage)
        elif parameter == 'password':
            update_password(email, users_storage)
        elif parameter == 'phone':
            update_phone(email, users_storage)
        else:
            print('Incorrect parameter.')
    else:
        print('User with this email does not exist.')


