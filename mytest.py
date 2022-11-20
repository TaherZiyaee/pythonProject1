# ls1=['a','b','c','d']
# for i,j in enumerate(ls1):
#     print(i,':',j)
from random import seed, random, uniform, randint

# seed(10)

dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, }
for _ in range(1000):
  dice[randint(1, 6)] += 1
print(dice)
