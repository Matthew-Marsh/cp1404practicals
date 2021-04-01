""" Program stores user's email and names in a dictionary. """


def main():
    """ Get user email and name then store in dictionary."""
    email_dict = {}
    # Request user email until blank is entered
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)

        name_confirmation = input("Is your name {}? (Y/n) ".format(name)).upper()
        if name_confirmation != "" and name_confirmation != "Y":
            name = input("Name: ")
        email_dict[email] = name
        email = input("Email: ")
    print()
    for email, name in email_dict.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Separates the name from the email and returns name"""
    email_parts = email.split("@")
    name = email_parts[0]
    name_parts = name.split(".")
    name = ' '.join(name_parts).title()
    return name


main()
