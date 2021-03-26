# 1.
numbers = []
for number in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

