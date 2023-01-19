lst = [1, 2, 3]

# print(lst)
# lst.clear()
# print(lst)

# lst1=lst.copy()
# lst1[0]=0
# print(lst)
# print(lst1)

# from copy import deepcopy
# lst1=[1,["A","B"],3]
# print(lst1)
# lst2=deepcopy(lst1)
# lst2[1][0]="H"
# print(lst2)

# lst1=[1,2,3,2,5,7,2,9]
# print(lst1.count(2))

# lst1 = [4, 5, 6]
# lst.extend(lst1)
# print(lst)

# lst_str = ["Ali", "Hassan", "Naghi", "Saeid"]
# print(lst_str.index("Naghi"))

# lst_str = ["Ali", "Hassan", "Naghi", "Saeid", "Hassan", "Javid"]
# print(lst_str.index("Hassan"))
# print(lst_str.index("Hassan", 2))
# print(lst_str.index("Javid", 1, 4))

# lst.insert(1, "a")
# print(lst)

# lst_str = ["Ali", "Hassan", "Naghi", "Saeid", "Hassan", "Javid"]
# print(lst_str.pop(3))
# print(lst_str)
# print(lst_str.pop())
# print(lst_str)

lst_str = ["Ali", "Hassan", "Naghi", "Saeid", "Hassan", "Javid"]
# lst_str.remove("Hassan")
# print(lst_str)

lst_str.reverse()
print(lst_str)
lst_str.sort()
print(lst_str)
lst_str.sort(reverse=True)
print(lst_str)