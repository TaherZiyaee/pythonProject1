# ------- start of Decorator -------
# def dec(func):
#     def inner():
#         print('*' * 10)
#         func()
#         print('*' * 10)
#
#     return inner
# #------- end of Decorator -------
#
# @dec
# def func():
#     print('TAHER')
#
# def func2():
#     print('NOYAN')
#
# func()
# func2()

# --------------------------------------
# ----- start of Decorator -------
def dec(func):
    def inner(a, b):
        if b == 0:
            return 'Warning !!!!!'
        return func(a, b)

    return inner
# ------- end of Decorator -------


@dec
def func(x, y):
    return x / y


print(func(5, 2))
print(func(5, 0))
