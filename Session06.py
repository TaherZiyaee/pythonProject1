# Ramznegari
# def encryptor_(mypass):
#     pass_ = mypass
#     textCrypted = ''
#     for c in pass_:
#         x = ord(c) + 4 * 3
#         textCrypted += chr(x)
#     return textCrypted
#
# print(encryptor_('taher zia'))
# --------------------------------

# def f(x):
#     return 2*x+1
# print(f(-2))

# --------------------------------
# def cube_(num1):
#     return pow(num1, 3)
#
# print(cube_(3))
#
# def myFunc():
#     pass
# --------------------------------

# def repeat(number, digit):
#     i=0
#     while number>0:
#         if number%10==digit:
#             i+=1
#         number//=10
#     return i
#
# number=int(input('Enter a number: '))
# digit=int(input('Enter a digit: '))
# print(digit,'is repeated',repeat(number,digit),'time(s).')

# --------------------------------
# Problem? 1! + 2! + 3! + ... n!
# Bar asase osoole Good Coding har tabe' bayad vazifeye khasi ra anjam dahad.
# Leza ma yek tabe' minevisim ke Factorial ra hesab konad & yek tabe' ke Factorial-ha ra ba ham + konad.
# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f
#
#
# def sum_fact(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += fact(i)
#     return s
#
#
# n = int(input('Enter fact number: '))
# print(f'Sum factorial {n}! = {sum_fact(n)}')
# --------------------------------

# def func(a, b, c):
#     print('a =', a)
#     print('b =', b)
#     print('c =', c)
#
#
# # normal
# func(2, 3, 5)
# # name = value
# func(b=4, c=11, a=-3)
# # normal + name = value
# func(2, b=2, c=6)
# # itrable - (str,list,tuple,set)
# func(*[4, 8, 15])
# x = [-3, 7, 17]
# func(*x)
# # **dict
# d = {'a': 4, 'b': 12, 'c': 1}
# func(**d)

# --------------------------------
# normal
# def func(a, b, c):
# # default value
# def func(a=3, b=-9, c=13):
# # # normal + name = value
# def func(a=3, b=-9, c=13):
# # *name
# def func(a, b, *c):
#     print('a =', a)
#     print('b =', b)
#     print('c =', c)
#
# func(2, 3)

# --------------------------------
# def func1(a, b, /, c,d,*,e,f,g):
# def func1(a, b, /, c):
#     print('a=', a)
#     print('c=', b)
#     print('c=', c)
#
# func1(4, 11, c=2)

# --------------------------------
# def max3(a,b,c):
#     """Recive three numbers as input and return the maximum of them
#
#     :parameter
#         a (int): A decimal integer
#         b (int): Another decimal integer
#         c (int): Another decimal integer
#
#     :return
#         max_int (int): Maximum of three numbers
#     """
#     return max(a,b,c)
#
# # print(max3.__doc__)
# print(help(max3))

# --------------------------------
# def func2(x:int,y:int,z:int):
#     print('x:',x)
#     print('y:',y)
#     print('z:',z)
#
# print(func2(2,5,'7'))

def funcSum(a: int = 4, b: int = 5, c: float = 32.4) -> tuple:
    return a + b + c, a, b, c


print(funcSum())
print(funcSum.__annotations__)
