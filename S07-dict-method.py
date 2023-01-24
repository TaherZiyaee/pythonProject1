dt = {"a": 1, "b": 2, "c": 3}
print(dt.fromkeys("b"))
print(dt.fromkeys(["b", "d", "e"]))
print(dict.fromkeys(["b", "d", "e"]))
print(dt.fromkeys(["b", "d", "e"], 7))

print(dt.get("c"))

print(dt.keys())
print(dt.values())
print(dt.items())

# print(dt.pop("b"))
# print(dt)

# print(dt.setdefault("c"))
# print(dt)
# print(dt.setdefault("p"))
# print(dt)
# print(dt.setdefault("s", 17))
# print(dt)

f = {"z": 11, "y": 12}
dt.update(f)
print(dt)
dt.update({"a":55,"x":13})
print(dt)
