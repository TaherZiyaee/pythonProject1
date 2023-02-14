# ls1=['a','b','c','d']
# for i,j in enumerate(ls1):
#     print(i,':',j)
from random import seed, random, uniform, randint

# seed(10)

# dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, }
# for _ in range(1000):
#   dice[randint(1, 6)] += 1
# print(dice)


# from texttable import Texttable
# t = Texttable()
# t.add_rows([['Name', 'Age'], ['Alice', 24], ['Bob', 19]])
# print(t.draw())

import mytest1
from random import *
mytest1.func1(2)
del mytest1
del random
mytest1.func1(3)


# func1(3)
# # del func1
# gc.collect()
# del gc
# gc.collect()
# # func1(4)








# a=10
# print("1",a)
# # del a
# gc.collect()
# print("2",a)