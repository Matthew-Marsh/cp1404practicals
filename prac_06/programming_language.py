""" Class will take in programming language and its attributes to process """

class ProgrammingLanguage:
    """ Programming language and its attributes  """

    def __init__(self, name, typing, reflection, year):
        """ Initialise programming language with attributes """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """ Print language and its attributes """
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """ Determine if the lagnuage is dynamic """
        return self.typing == 'Dynamic'
