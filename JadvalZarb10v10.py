ls = list(map(int, input('Enter a,b: ').split(',')))
i, k = 1, 1
while k <= ls[1]:
    if k == 1:
        print(f'\t{k}\t', end='')
    else:
        print(k, end='\t')
    k += 1
print()
while i <= ls[0]:
    print(i, end='\t')
    j = 1
    while j <= ls[1]:
        print(i * j, end='\t')
        j += 1
    print()
    i += 1
