"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))

    print_message = determine_result(score)
    print("\t{}".format(print_message))

    score = random.randint(0, 101)
    print_message = determine_result(score)
    print("Score {}: \n\t{}".format(score,print_message))


def determine_result(score):
    print_message = "Invalid score"
    if score <= 100 and score >= 90:
        print_message = "Excellent"
    elif score >= 50 and score < 90:
        print_message = "Passable"
    elif score < 50 and score >= 0:
        print_message = "Bad"
    return print_message


main()
