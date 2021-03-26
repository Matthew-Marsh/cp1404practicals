import random

NUMBER_OF_NUMBERS = 6
LARGEST_NUMBER = 45
SMALLEST_NUMBER = 1

number_of_picks = int(input("How many quick picks? "))
random_numbers = []
for number in range(number_of_picks):
    random_numbers = [random.randint(SMALLEST_NUMBER, LARGEST_NUMBER) for number in range(NUMBER_OF_NUMBERS)]
    random_numbers.sort()
    for number in random_numbers:
        print("{:>2}".format(number), end=" ")
    print()
