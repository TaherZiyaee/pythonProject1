# ---------------- 1 -----------------
# def myLen(myString):

# ---------------- 4 -----------------
# flag=False
# def check_cube(myDigit):
#     for i in range(1,myDigit//2):
#         if i**2 == myDigit:
#             global flag
#             flag=True
#             break
#     return i
# myDigit=int(input('Enter your entry: '))
# result=check_cube(myDigit)
# if flag == True:
#     print(f'{result} is cube of {myDigit} .')
# else:
#     print(f'{myDigit} does not have any cube entry!')

# ---------------- 5 -----------------
# def check_isdigit(entry):
#     try:
#         val=int(entry)
#         return val
#     except ValueError:
#         print("No.. input is not a number. It's a string")
#         exit(14)
#
# def discount_calculator(price: int, percentage: int):
#     if not (0 <= percentage <= 100):
#         print('Your Present entry is not valid !\nPlease try again ...')
#         exit(13)
#     return price - (price * percentage / 100)
#
# price=input('Enter the price: ')
# price=check_isdigit(price)
# percentage=input('Enter the percentage: ')
# percentage=check_isdigit(percentage)
# round_price=round(discount_calculator(price,percentage))
# print(f'{price:,}$ with {percentage}% off is {round_price:,}$ .')

# ---------------- 6 -----------------
def check_entry(entry: str):
    if entry.isdigit():
        return 'digit'
    elif entry.islower():
        return 'lower case character'
    elif entry.isupper():
        return 'upper case character'
    else:
        return 'other symbol'
