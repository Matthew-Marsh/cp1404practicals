"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. When will a ValueError occur?
# A ValueError will occur when the incorrect type is entered, i.e. String when it's an Int
#
# 2. When will a ZeroDivisionError occur?
# This error will occur when attempting to divide a number by zero.
#
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# You could use a while error check on denominator to ensure a zero wasn't entered.
