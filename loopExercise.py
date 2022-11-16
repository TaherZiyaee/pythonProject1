# ------------------1--------------------
# Print numbers between 2 numbers
# برنامه اي بنويسيد كه دو عدد را از كاربر گرفته و اعداد مابين آن ها را نمايش دهد
# ln1 = list(map(int, input('Enter 2 number: ').split(',')))
# print(ln1)
# for i in range(ln1[0]+1, ln1[1]):
#     print(i, end=' ')

# ------------------2--------------------
# برنامه اي بنويسيد كه دو عدد صحيح را گرفته و مقسوم عليه هاي مشتركشان را نمايش دهد
ls1, ls2 = [], []
ln1 = list(map(int, input('Enter 2 number: ').split(',')))
for i in range(1, ln1[0] + 1):
    if ln1[0] % i == 0:
        ls1.append(i)
for i in range(1, ln1[1] + 1):
    if ln1[1] % i == 0:
        ls2.append(i)
print(ln1[0], ls1, '\n', ln1[1], ls2, sep='')
s1 = set(ls1).intersection(set(ls2))
print(s1)

# ------------------3--------------------
# برنامه اي بنويسيد كه دو عدد صحيح را گرفته و بزرگترين مقسوم عليه مشتركشان را نمايش دهد
print('MAX =', max(s1))
