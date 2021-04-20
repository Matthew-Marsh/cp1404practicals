""" Tests the Guitar class and methods """
from prac_06.guitar import Guitar


def main():
    """ Store guitar information and then test Guitar methods """
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    another_guitar = Guitar("Another Guitar", 2013, 10.5)
    print("{} get_age() - expected 99. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - expected 8. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage() - expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


if __name__ == '__main__':
    main()
