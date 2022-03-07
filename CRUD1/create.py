def unique_check(email, user_emails):
    if email in user_emails:
        return False
    else:
        return True


def create_user(email, name, password, phone, user_emails, users_storage):
    if unique_check(email, user_emails):
        user_emails.append(email)
        users_storage[email] = {"name": name,
                                "password": password,
                                "phone": phone}
    else:
        print('This email already exists. Please, enter another email.')
