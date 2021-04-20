""" Class stores guitar information for processing. """


class Guitar:
    """ Class stores guitar attributes for processing """

    CURRENT_YEAR = 2021

    def __init__(self, name="", year=0, cost=0):
        """ Initialize guitar details """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ Print guitar details """
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """ Determine the guitar age """
        return Guitar.CURRENT_YEAR - self.year

    def is_vintage(self):
        """ Determine if guitar is vintage """
        return self.get_age() >= 50
