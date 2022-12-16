# i = [1, 2, 3]
# i = iter(i)
# print(i.__next__())
# print(next(i))
# print(next(i))

# i = [1, 2, 3]
# i = iter(i)
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break

from itertools import count
counter=count(10)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

