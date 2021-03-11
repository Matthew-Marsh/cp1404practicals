in_file = open("on_off.txt", 'r')
try:
    program_on = out_file.readline()
except:
    program_on = False
out_file = open("on_off.txt", 'w')
if program_on:
    print("False", file=out_file, end='')
else:
    print("True", file=out_file, end='')
out_file.close()
in_file.close()
