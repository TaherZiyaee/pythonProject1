# def func(x):
# return x ** 2

# def func2(x):
#     return x > 5
#
#
# li = [1, 5, 8, 3, 6, 12, 5, 2, 9]
# print(li)
# new = list(filter(func2, li))
# print(new)

# from functools import reduce
#
# li = [1, 2, 3, 4]
# print(li)
# mysum = reduce(lambda x, y: x + y, li)
# print(mysum)

# li = [3, 54, -3, 6, 12, 4, 0, 41, -90, 3]
# print(li)
# new = sorted(li)
# print(new)

li = ['kjcfdh', 'saddaswq', 'dsa', 'jahsbdg', 'jhbjhsajhbshs', 'ds']
print(li)
new = sorted(li, key=len)
print(new)
