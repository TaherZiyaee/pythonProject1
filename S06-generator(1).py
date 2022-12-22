# def func(x):
#     print('Hello')
#     yield x ** 2
#     print('Taher')
#     yield 17
#     print('Ziaei')
#     yield x - 2
#
#
# x = func(5)
# print(next(x))
# print(next(x))
# print(next(x))

# --------------------------------
def my_generator():
    print('Welcome!')
    for i in range(5):
        yield i ** 2


g = my_generator()
for i in g:
    print(i)
