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
# def sum_gen(lst):
#     s=0
#     for i in lst:
#         s+=i
#         yield s
#
# lst=[1,2,3,4,5]
# sum1=sum_gen(lst)
# for i in sum1:
#     print(i)

# -------------- 4 -------------
# def string_revers(str1):
#     l=len(str1)
#     for i in range(l-1,-1,-1):
#         yield str1[i]
#
# sr=string_revers('TAHER')
# for i in sr:
#     print(i,end='')

# -------------- 5 -------------
# def my_gen(even_or_odd='e'):
#     c=0
#     if even_or_odd=='o':
#         c=1
#     while True:
#         yield c
#         c+=2
#
#
# mg=my_gen('e')
# for i in range(10):
#     print(next(mg))

# -------------- 6 -------------
def seq_gen():
    c=1
    while True:
        s=''
        for i in range(1,c+1):
            s+=f'{c}\t'
        yield s
        c+=1

sg=seq_gen()
for _ in range(10):
    print(next(sg))

