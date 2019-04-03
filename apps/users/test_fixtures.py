DATA_SUPERADMIN_INPUT = {
    'username': 'admin', 'email': 'admin@admin.com', 'password': 'admin123',
}
DATA_SUPERADMIN_OUTPUT = {
    'id': 1, 'username': 'admin', 'first_name': None,
    'last_name': None, 'birth_date': None, 'phone': None,
    'email': 'admin@admin.com', 'avatar': None, 'linkedin': None,
    'twitter': None, 'facebook': None, 'github': None,
}

DATA_USERS = [
    {
        'username': 'Alex', 'email': 'alex@gmail.com',
        'last_name': 'Petrov', 'password': '1234',
    },
    {
        'username': 'John', 'email': 'john@gmail.com',
        'last_name': 'Ivanov', 'password': '1234',
    },
    {
        'username': 'Tyler', 'email': 'tyler@gmail.com',
        'last_name': 'Sidorov', 'password': '1234',
    },
]
DATA_USER_OUTPUT = {
    'id': 2, 'username': 'Alex', 'first_name': None,
    'last_name': 'Petrov', 'birth_date': None, 'phone': None,
    'email': 'alex@gmail.com', 'avatar': None, 'linkedin': None,
    'twitter': None, 'facebook': None, 'github': None,
}


DATA_REGISTER_MISSED_EMAIL = {
    'username': 'mike', 'last_name': 'Tyson', 'password': '1234',
}

DATA_LOGIN_CORRECT = {
    'username': 'admin', 'password': 'admin123',
}

DATA_CHECK_USERNAME_INPUT = {'username': 'admin'}
DATA_CHECK_USERNAME_OUTPUT = {'is_reserved': False}

DATA_UPDATE_INPUT = {
    'first_name': 'John', 'last_name': 'Gold',
}
DATA_UPDATE_OUTPUT = {
    'id': 2, 'username': 'Alex', 'first_name': 'John',
    'last_name': 'Gold', 'birth_date': None, 'phone': None,
    'email': 'alex@gmail.com', 'avatar': None, 'linkedin': None,
    'twitter': None, 'facebook': None, 'github': None,
}
