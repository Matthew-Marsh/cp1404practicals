# Task 1:
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file=out_file, end='')
out_file.close()

# Task 2:
in_file = open("name.txt", "r")
name = in_file.readline()
print("Your name is {}".format(name), end='')
in_file.close()

# Task 3:
in_file = open("numbers.txt", "r")
result = 0
for i in range(2):
    result += int(in_file.readline())
print("Result is: {}".format(result))
in_file.close()

# Task 4:
in_file = open("numbers.txt", "r")
result = 0
for line in in_file:
    result += int(line)
print("Result is: {}".format(result), end="")
in_file.close()
