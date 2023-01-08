# ye adad migirad & tamame a'dade bozorgtar az 4 ra dar ham zarb mikonad
# def mul5(n):
#     if n == 0:
#         return 1
#     elif n % 10 < 5:
#         return mul5(n // 10)
#     else:
#         return n % 10 * mul5(n // 10)
#
#
# print(mul5(4238764237))

# ---------------------------------
# tamame adadhaye gochektar az an adad ke mazrabe 3 hastand ra chap konad
# def maz3(n):
#     if n<3:
#         return
#     elif n%3==0:
#         print(n)
#     maz3(n-1)
#
# maz3(20)

# ---------------------------------
# jam'e jomleye N-om ra namayesh dahad
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(8))
