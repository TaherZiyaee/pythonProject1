#---------------- 1 -----------------
# def myLen(myString):

# ---------------- 1 -----------------
flag=False
def check_cube(myDigit):
    for i in range(1,myDigit//2):
        if myDigit // i == i:
            global flag
            flag=True
            break
    return i
myDigit=int(input('Enter your number: '))
result=check_cube(myDigit)
if flag == True:
    print(f'{result} is cube of {myDigit} .')
else:
    print(f'{myDigit} does not have any cube number!')