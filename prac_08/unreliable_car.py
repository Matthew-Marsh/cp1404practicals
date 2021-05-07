""" Determine car reliability. """
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """ Calculate the reliability of a Car object. """

    def __init__(self, name, fuel, reliability):
        """ Initialise car instance details based on Car parent class. """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1, 100) < self.reliability:
            return distance
        return 0
