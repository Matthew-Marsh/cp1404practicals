MIN_PASSWORD_LENGTH = 10


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Password (min. length: {}): ".format(MIN_PASSWORD_LENGTH))
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Password must be {} characters long.".format(MIN_PASSWORD_LENGTH))
        password = input("Password (min. length: {}): ".format(MIN_PASSWORD_LENGTH))
    return password


main()
