# f = open("note10.txt", "rb")
# print(f.tell())
# print(f.read(17))
# f.seek(-3, 2)
# print(f.tell())
# print(f.read(5))

# import os
# if os.path.exists("note2.txt"):
#     f=open("note2.txt","r")
#     print(f.readlines())

import os
os.remove("note2.txt")