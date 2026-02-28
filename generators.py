import random
import string


def generate_email():
    login_letters = ''.join([random.choice(string.ascii_letters) for x in range(3)])
    login_digits = str(random.randint(100, 999))
    login = login_letters + login_digits + '@ya.ru'
    
    return login


def generate_password():
    password = str(random.randint(100000, 9999999))

    return password
