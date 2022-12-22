# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
#
# x = range(10, 20, 2)
# print(list(x))
#
# y = list_range(10, 20, 2)
# print(y)

# -------------------------------
from functools import wraps
from time import perf_counter


def time_caculation(func):
    @wraps(func)
    def wrapper_generator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print('The run time of', func.__name__, 'is:', run_time)
        return value

    return wrapper_generator


@time_caculation
def gen_range(start, end, step=1):
    while start < end:
        yield start
        start += step

@time_caculation
def org_range(x):
    lr = range(1, x)
    print(list(lr))

g = gen_range(1, 10000)
print(list(g))

org_range(10000)
