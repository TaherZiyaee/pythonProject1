# ls = ['taher', 'mozhgan', 'noyan', 'tahmoures']
# i = 0
# while i < len(ls):
#     s = ls[i]
#     j = 0
#     while j < len(s):
#         if not (j % 2 == 0):
#             print(s[j].upper(), end='')
#         else:
#             print(s[j], end='')
#         j += 1
#     print()
#     i += 1

#------------------------

from termcolor import colored
from colorama import Fore,Back
print(colored("Hi baby","red"))
print(Fore.RED+"ISC")