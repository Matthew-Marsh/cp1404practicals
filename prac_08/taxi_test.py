""" Program to test the taxi class. """
from prac_08.taxi import Taxi


def main():
    """Test the taxi and car classes."""
    taxi = Taxi('Prius 1', 100, 1.23)
    taxi.drive(40)
    print("{} Total: ${:.2f}".format(taxi, taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print("{} Total: ${:.2f}".format(taxi, taxi.get_fare()))


if __name__ == '__main__':
    main()
