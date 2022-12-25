# -------------- 1 -------------
# def my_enumerate(itrable, start=0):
#     for i in itrable:
#         yield start, i
#         start += 1
#
#
# s = 'ALI'
# lr = my_enumerate(s, 10)
# print(list(lr))

# -------------- 2 -------------
# def fibonachi():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# fib = fibonachi()
# for _ in range(10):
#     print(next(fib), end=' ')

# -------------- 3 -------------