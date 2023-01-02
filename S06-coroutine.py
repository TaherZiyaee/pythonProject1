# def my_gen():
#     print('Start !!!!')
#     while True:
#         name = yield 4
#         print('My name is',name)
#
# g = my_gen()
# print(next(g))
# g.send('Taher')
# g.send('Noyan')

#------------------------------------
from functools import wraps
def crotouine(func):
    @wraps(func)
    def start(*args,**kwargs):
        gn=func()
        next(gn)
        return gn
    return start

@crotouine
def my_gen():
    print("Start !!!")
    for i in range(10):
        name = yield i
        print('My name is',name)

g=my_gen()
print(g.send('Taher'))
print(g.send('Noyan'))
print(g.send('Mozhgan'))


