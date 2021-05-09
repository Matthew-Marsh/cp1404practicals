""" Program to test the Silver Service Taxi class. """
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the Silver Service Taxi and parent classes."""
    new_taxi = SilverServiceTaxi('Mitsubishi', 100, 2)
    new_taxi.drive(18)
    print("{} Total: ${:.2f}".format(new_taxi, new_taxi.get_fare()))


if __name__ == '__main__':
    main()
