from sys import stdin, stdout, stderr

# f = stdin.readline()
# print(f)
#
# stdout.write("Hello!")
#
# stderr.write("ERROR!")


# stdout_temp = stdout
# stdout = open("note2.txt", "w")
# stdout.write("Manchester United")
# stdout = stdout_temp

# stdin_temp = stdin
# stdin = open("note10.txt", "r")
# line = stdin.readline()
# print(line)
# stdin = stdin_temp

f = open("note2.txt", "w")
print(1, 2, 3, 4, sep="-", file=f)
