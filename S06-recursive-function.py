# def fact(x):
#     if x == 0 or x == 1:
#         return 1
#     return x * fact(x - 1)
#
#
# print(fact(5))

# ----------------------------
# from time import sleep
#
#
# def reverse(n):
#     if n < 0:
#         return
#     sleep(1)
#     print(f"\r{n}", end="")
#     n -= 1
#     reverse(n)
#
#
# reverse(5)

# ----------------------------
from time import sleep

def job_precent(n=0):
    if n > 100:
        return
    print(f"\rYou have finished %{n}", end="")
    n += 5
    sleep(0.5)
    job_precent(n)


job_precent()

# ----------------------------
