"""
Program provide a list of taxi choices and then calculate the fare based on distance
travelled in chosen taxi.
"""
__author__ = 'Matthew Marsh'

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Get taxi choice and distance, then display the fare total."""
    current_taxi = None
    menu_choice = None
    fare_total = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    while menu_choice != 'q':
        try:
            print("q)uit, c)hoose taxi, d)rive")
            menu_choice = input(">>> ")
            if menu_choice == 'c':
                current_taxi = get_taxi_choice(taxis)
            elif menu_choice == 'd':
                if current_taxi is None:
                    print("You need to choose a taxi before you can drive.")
            else:
                print("Invalid option")
            print("Bill to date: ${:.2f}".format(fare_total))

        except IndexError:
            print('Invalid taxi choice')
        except ValueError:
            print("Taxi choice must be a number.")


def get_taxi_choice(taxis):
    """Display list of taxis and return chosen taxi"""
    print("Taxi's available:")
    for i, taxi in enumerate(taxis):
        print(i, '-', taxi)
    taxi_choice = int(input("Choose taxi: "))
    return taxis[taxi_choice]


if __name__ == '__main__':
    main()
