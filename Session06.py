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
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def sum_fact(n):
    s = 0
    for i in range(1, n + 1):
        s += fact(i)
    return s


n = int(input('Enter fact number: '))
print(f'Sum factorial {n}! = {sum_fact(n)}')
