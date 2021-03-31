""" Program stores user's email and names in a dictionary. """


def main():
    """ Get user email and name then store in dictionary."""
    # Request user email until blank is entered
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        print(name)
        email = input("Email: ")


def get_name_from_email(email):
    email_parts = email.split("@")
    name = email_parts[0]
    name_parts = name.split(".")
    name = ' '.join(name_parts).title()
    return name


main()
