"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

print_message = "Invalid score"
if score <= 100 and score >= 90:
    print_message = "Excellent"
elif score >= 50 and score < 90:
    print_message = "Passable"
elif score < 50 and score >= 0:
    print_message = "Bad"

print(print_message)
