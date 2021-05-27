"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
Modifications by Matthew Marsh
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    strings = [s for _ in range(n)]
    return ' '.join(strings)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(sentence):
    """
    Format the sentence so that it begins with a capital and ends with a period
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("the dog ran to the ball")
    'The dog ran to the ball.'
    """
    sentence = sentence.split(' ')
    sentence[0] = sentence[0].title()
    if sentence[-1][-1:] != '.':
        sentence[-1] = sentence[-1] + '.'
    sentence = ' '.join(sentence)
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert tests with custom message,
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    assert test_car.fuel == 0, "Car does not set fuel by default correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel to the passed in value correctly"


run_tests()

doctest.testmod()
