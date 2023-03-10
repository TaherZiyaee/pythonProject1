class A:
    def __enter__(self):
        print("start!")
        return 17

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end!")


with A() as x:
    print("I am Taher.")
    print("Welcome!")
    print(x)

f = open("note10.txt", "r")
print(dir(f))

with open("note1.txt", "w") as f:
    f.write("Hi baby!")

with open("note.txt", "r") as f1, open("note2.txt", "w") as f2:
    for line in f1:
        print(line, end="")
        f2.write(line)
    f2.write("\n-------")
