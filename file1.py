ch = chr(5717)
# f = open("note10.txt", "a", encoding="utf-8")
# f.write("\n" + ch)

# f = open("note10.txt", "r", encoding="utf-8")
# print(f.read())

# f = open("note10.txt", "ab")
# s = b"\ntaher"
# f.write(s)
#
# if f.writable():
#     f.write("Jasem")
#
# if f.readable():
#     f.read()

# f = open("note10.txt", "r", encoding="utf-8")
# print(f.read(2))

# f = open("note.txt", "r", encoding="utf-8")
# print(f.readline(),end="")
# print(f.readline(),end="")

# f = open("note.txt", "r", encoding="utf-8")
# lst = f.readlines()
# for snt in lst:
#     print(snt, end="")

f = open("note.txt", "r", encoding="utf-8")
for line in f:
    print(line,end="")