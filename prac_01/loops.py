for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.

number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

# d.

number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars+1, 1):
    print("*" * i)
