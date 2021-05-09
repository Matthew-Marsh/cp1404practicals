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
    fare_total = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != 'q':
        try:
            if menu_choice == 'c':
                current_taxi = get_taxi_choice(taxis)
            elif menu_choice == 'd':
                if current_taxi is None:
                    print("You need to choose a taxi before you can drive.")
                else:
                    fare = calculate_fare_total(current_taxi)
                    print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                    fare_total += fare
            else:
                print("Invalid option")
            print("Bill to date: ${:.2f}".format(fare_total))
            print("q)uit, c)hoose taxi, d)rive")
            menu_choice = input(">>> ").lower()
        except IndexError:
            print('Invalid taxi choice')
        except ValueError:
            print("Taxi choice must be a number")
    print("Total trip cost: ${:.2f}".format(fare_total))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(i, '-', taxi)


def get_taxi_choice(taxis):
    """Display list of taxis and return chosen taxi"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(i, '-', taxi)
    taxi_choice = int(input("Choose taxi: "))
    return taxis[taxi_choice]


def calculate_fare_total(taxi):
    fare_total = 0
    taxi.start_fare()
    while fare_total == 0:
        try:
            distance = float(input("Drive how far? "))
            taxi.drive(distance)
            fare_total = taxi.get_fare()
            return fare_total
        except ValueError:
            print("Distance must be a number")


if __name__ == '__main__':
    main()
