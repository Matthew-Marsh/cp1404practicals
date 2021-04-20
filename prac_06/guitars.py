""" Gets guitar details from user and processes them with Guitar class. """
from prac_06.guitar import Guitar


def main():
    """ Get guitar details from user and process with Guitar class """
    guitars = []

    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print("{} ({}) : ${:.2f} added.".format(guitar_name, guitar_year, guitar_cost))
        print()
        guitar_name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{}".format(i, vintage_string,
                                                                                                   guitar=guitar))


if __name__ == '__main__':
    main()
