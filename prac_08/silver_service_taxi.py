""" Determine how much the fare is based on the level of fanciness. """
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ Specialised instance of a Taxi with included fare costs and modifications. """
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness='0.0'):
        """ Initialise silver service taxi instance details based on Taxi parent class. """
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                    SilverServiceTaxi.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + SilverServiceTaxi.flagfall
