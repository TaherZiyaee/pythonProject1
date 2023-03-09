# f = open("note10.txt", "w")
# f.write("Taher Ziaei\n")
# f.write("Noyan Ziaei\n")
# f.flush()
# input("Continue...")
# f.close()

# f = open("note10.txt", "wb", buffering=0)
# f.write(b"Bruno Fernandez\n")
# f.write(b"David Degea\n")
# f.write(b"Marcus Rashford\n")
# input("Continue...")
# f.close()

# import io
# print(io.DEFAULT_BUFFER_SIZE)

# f = open("note10.txt", "r", encoding="utf-8")
# print(f.tell())
# print(f.readline(), end="")
# print(f.tell())
# print(f.readline(), end="")

# f = open("note1.txt", "w", encoding="utf-8")
# print(f.tell())
# f.write("ည")
# print(f.tell())
# print(bytes("ည", "utf-8"))


import os
print(repr(os.linesep))
