# --------------- 1 ---------------
# from functools import wraps
#
# users = {'taher': '7621345', 'hossein': '87sfd', 'masoud': 'fds76sd'}
# blacklist = {'taher'}
#
#
# def block_user(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         if args[0] in blacklist:
#             print('sorry,', args[0], 'is blocked !!')
#         else:
#             func(*args, **kwargs)
#
#     return wrapper_decorator
#
#
# @block_user
# def show_password(username):
#     print(username, ':', users[username])
#
# @block_user
# def change_password(username, new_password):
#     users[username] = new_password
#     print(users)
#
#
# show_password('taher')
# change_password('taher', '123')

# --------------- 2 ---------------
from functools import wraps
from time import perf_counter


def time_calculation(func):
    @wraps(func)
    def wrraper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print('The run time of', func.__name__, 'is:', run_time)
        return value

    return wrraper_decorator


@time_calculation
def A(x):
    s = 0
    for i in range(x):
        s += i ** 2


@time_calculation
def B(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i


A(10000)
B(100)
