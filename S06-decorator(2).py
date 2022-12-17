# def dec(func):
#     def inner(*x, **y):
#         if y == 0:
#             return 'Warning !!!!'
#         return func(*x, **y)
#
#     return inner
#
# @dec
# def func(x, y, z):
#     return x * y + z['A']
#
# print(func(2, 5, {'A': 3}))

#---------------------------------------------
def dash(func):
    def inner(*x,**y):
        print('-'*15)
        func(*x,**y)
        print('-' * 15)
    return inner

def plus(func):
    def inner(*x,**y):
        print('+'*15)
        func(*x,**y)
        print('+' * 15)
    return inner

def star(func):
    def inner(*x,**y):
        print('*'*15)
        func(*x,**y)
        print('*' * 15)
    return inner

# @dash
# @plus
# @star
def msg(name):
    print('I am',name)

# msg('Taher')

printer=dash(plus(star(msg)))
printer('Taher')