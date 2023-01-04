def func():
    "doc.."
    pass


print(dir(func))  # Faghat esme tabe ra minevisim. bedoone parantez
print(func.__name__)
print(func.__doc__)


def ave(lst):
    return sum(lst) / len(lst)


def ave2(lst):
    return sum(lst) / len(lst)


ave.school_name = "Peyvand"
ave2.school_name = "Kar & Danesh"

print(ave.school_name)
print(ave2.school_name)

setattr(ave, "school_name", "Peyvand")
print(ave.school_name)

setattr(ave, "school_name", "Peyvand")
setattr(ave, "location", "Gorgan")
print(ave.__dict__)

print(getattr(ave, "school_name"))

print(getattr(ave, "name", "None"))

if hasattr(ave, "name"):
    print(getattr(ave, "name"))

delattr(ave, "school_name")
