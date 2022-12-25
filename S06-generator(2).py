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
# from functools import wraps
# from time import perf_counter
#
#
# def time_caculation(func):
#     @wraps(func)
#     def wrapper_generator(*args, **kwargs):
#         start_time = perf_counter()
#         value = func(*args, **kwargs)
#         end_time = perf_counter()
#         run_time = end_time - start_time
#         print('The run time of', func.__name__, 'is:', run_time)
#         return value
#
#     return wrapper_generator
#
#
# @time_caculation
# def gen_range(start, end, step=1):
#     while start < end:
#         yield start
#         start += step
#
#
# @time_caculation
# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
#
# end_number = 10000000
#
# gen_range(1, end_number)
#
# list_range(1, end_number)

# -------------------------------
# def my_generator(r=10):
#     for i in range(r):
#         yield i ** 2


# g = my_generator()
# print(list(g))
# print(list(g))
# print(max(g))
# print(min(g))
# print(sum(g))

# print(next(g))
# print(next(g))
# print(next(g))
# g.close()
# print(next(g))
# g.send()
# for i in g:
#     if i==16:
#         g.throw(ValueError('My Error'))
#     print(i)

# -------------------------------
def square_gn(lnum):
    for i in lnum:
        yield i ** 2


def even_gn(lnum):
    for i in lnum:
        if i % 2 == 0:
            yield i


lr = [1, 3, 5, 7, 2, 4, 3, 9, 6, 1, 3]
print(sum(even_gn(square_gn(lr))))
