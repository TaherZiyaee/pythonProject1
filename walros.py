x = []
while (s := input("Enter names (q for quit): ").lower()) != "q":
    x.append(s)

print("list:", x)


x = []
while True:
    s=input("Enter names (q for quit): ").lower()
    if s == "q":
        break
    x.append(s)

print("list:", x)