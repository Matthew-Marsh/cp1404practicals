def main():
    numbers = [-5, 9, -3, 3, 2, 8, -2]
    display(numbers)


def display(numbers):
    negative_numbers = []
    positive_numbers = []
    for number in numbers:
        if number < 0:
            negative_numbers.append(number)
        elif number > 0:
            positive_numbers.append(number)
    print("Negative Numbers")
    print([number for number in negative_numbers])

    print("Positive Numbers")
    print([number for number in positive_numbers])


main()
