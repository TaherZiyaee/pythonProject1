# ------------------1--------------------
# Print numbers between 2 numbers
# برنامه اي بنويسيد كه دو عدد را از كاربر گرفته و اعداد مابين آن ها را نمايش دهد
# ln1 = list(map(int, input('Enter 2 number: ').split(',')))
# print(ln1)
# for i in range(min(ln1)+1, max(ln1)):
#     print(i, end=' ')

# ------------------2--------------------
# برنامه اي بنويسيد كه دو عدد صحيح را گرفته و مقسوم عليه هاي مشتركشان را نمايش دهد
# ls1, ls2 = [], []
# ln1 = list(map(int, input('Enter 2 number: ').split(',')))
# for i in range(1, ln1[0] + 1):
#     if ln1[0] % i == 0:
#         ls1.append(i)
# for i in range(1, ln1[1] + 1):
#     if ln1[1] % i == 0:
#         ls2.append(i)
# print(ln1[0], ls1, '\n', ln1[1], ls2, sep='')
# s1 = set(ls1).intersection(set(ls2))
# print(s1)
# ------------ Halate behineh --------------
# for i in range(1,min(ln1)+1):
#     if ln1[0] % i == 0 and ln1[1] % i == 0:
#         print(i,end=' ')

# ------------------3--------------------
# برنامه اي بنويسيد كه دو عدد صحيح را گرفته و بزرگترين مقسوم عليه مشتركشان را نمايش دهد
# print('MAX =', max(s1))

# ------------------4--------------------
# برنامه اي بنويسيد كه دو عدد صحيح را گرفته و كوچكترين مضرب مشتركشان را نمايش دهد
# ln1 = list(map(int, input('Enter 2 number: ').split(',')))
# i=1
# s1=set()
# s2=set()
# while True:
#     s1.add(ln1[0]*i)
#     s2.add(ln1[1]*i)
#     if s1.intersection(s2):
#         sha=s1.intersection(s2)
#         break
#     i+=1
# print(sha)

# ------------------5--------------------
# num=int(input('Enter a number: '))
# i=0
# while num>0:
#     num //= 10
#     i+=1
# print(i)
# ------------------6--------------------
# برنامه ای که تعداد سطر را از کاربر گرفته و شکل زیر را رسم کند
n = int(input('Enter row#: '))
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * i)

# ------------------6--------------------
# from random import choice
#
# familyTuple=('Ali', 'Taher', 'Mozhgan', 'Noyan', 'Mojtaba'
#           ,'Morteza','Mostafa','Tahmouress','Elahe','Avina')
# systemGuessTuple=set()
# print(familyTuple)
# i=1
# while i<=len(familyTuple):
#     name=choice(familyTuple)
#     if name in systemGuessTuple:
#         continue
#     systemGuessTuple.add(name)
#     print(f'{i}: {name}')
#     ans=input('Is it true? (y/n) ')
#     if ans.lower()=='y':
#         print('*'*5,'FINISH','*'*5)
#         print(f'{name} is the name.')
#         exit(0)
#     i+=1
# print('Are you kidding me!')
# exit(13)
