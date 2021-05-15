""" Determine if car will drive a distance based on reliability. """
from prac_08.unreliable_car import UnreliableCar
import random
MINIMUM_DRIVE = 1
MAXIMUM_DRIVE = 200


def main():
    """Test car reliability class with car instances."""
    honda = UnreliableCar('Honda', 200, 20)
    toyota = UnreliableCar('Toyota', 250, 90)

    honda_distance = honda.drive(random.randint(MINIMUM_DRIVE, MAXIMUM_DRIVE))
    toyota_distance = toyota.drive(random.randint(MINIMUM_DRIVE, MAXIMUM_DRIVE))
    if honda_distance == 0:
        print("Honda was a piece of junk and couldn't drive", end="")
        honda_drove = False
    else:
        print("Honda managed to drive {} kms".format(honda_distance), end="")
        honda_drove = True

    if toyota_distance == 0:
        if not honda_drove:
            print(", and the Toyota didn't make it anywhere either.")
        else:
            print(", but the Toyota didn't move anywhere.")
    else:
        if not honda_drove:
            print(" but the Toyota managed to drive {} kms.".format(toyota_distance), end="")
        else:
            print(" and the Toyota also managed to drive {} kms.".format(toyota_distance))


if __name__ == '__main__':
    main()
