# ---------------- 1 -----------------
# def myLen(it):
#     counter=0
#     for _ in it:
#         counter+=1
#     return counter
#
# # myString=(input('Enter your string: '))
# # print(f'Lenghth of your string is {myLen(myString)}')
#
# l1=[3,6,78,1,6]
# t1=(3,31,6,74)
# d1={'a':4,'b':5}
# print(myLen(l1))
# print(myLen(t1))
# print(myLen(d1))

# ---------------- 2 -----------------
# def max2(it):
#     big=it[0]
#     for i in it:
#         if i > big:
#             big=i
#     return big
#
# t1=tuple(map(int,input('Enter your numbers:').split(' ')))
# print(max2(t1))

# ---------------- 3 -----------------
# def sum2(it):
#     mysum = 0
#     for i in it:
#         mysum += i
#     return mysum
# t1 = tuple(map(int, input('Enter your numbers:').split('+')))
# print(f'Sum of your numbers is {sum2(t1)}')

# ---------------- 4 -----------------
# def check_square(myDigit):
#     for i in range(1, myDigit // 2):
#         if i ** 2 == myDigit:
#             print(f'Yes! {i} * {i} = {myDigit}')
#             break
#     else:
#         print(f'{myDigit} does not have any cube entry!')
#
#
# myDigit = int(input('Enter your entry: '))
# check_square(myDigit)

# ---------------- 5 -----------------
def check_isdigit(entry):
    try:
        val=int(entry)
        return val
    except ValueError:
        print("No.. input is not a number. It's a string")
        exit(14)

def discount_calculator(price: int, percentage: int):
    if not (0 <= percentage <= 100):
        print('Your Present entry is not valid !\nPlease try again ...')
        exit(13)
    return price - (price * percentage / 100)

price=input('Enter the price: ')
price=check_isdigit(price)
percentage=input('Enter the percentage: ')
percentage=check_isdigit(percentage)
round_price=round(discount_calculator(price,percentage))
print(f'{price:,}$ with {percentage}% off is {round_price:,}$ .')

# ---------------- 6 -----------------
# def check_entry(entry: str):
#     if entry[0].isdigit():
#         return 'digit'
#     elif entry[0].islower():
#         return 'lower case character'
#     elif entry[0].isupper():
#         return 'upper case character'
#     else:
#         return 'other symbol'
#
# print('If enter string, just will check fist character of the string !')
# mychar=input('Enter your character (): ')
# result=check_entry(mychar)
# print(f'Your character is {result}.')
