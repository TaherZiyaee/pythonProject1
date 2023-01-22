# print(dir(tuple))
#
# tpl = (1, 2, 3, 4, 5, 3, 7, 6, 3, 5, 1, 3, 6)
# print(tpl.count(3))
# print(tpl.index(7))

print(dir(set))
# st={1, 2, 3, 4, 5,  5, 1, 3, 6}
# print(st)
# st.clear()
# print(st)
#
# st={1, 2, 3, 4, 5,  5, 1, 3, 6}
# print(st)
# st.add(8)
# print(st)

# st = {1, 2, 3, 4, 5, 5, 1, 3, 6}
# xt = st
# xt.add(11)
# print("ST:", st)
# print("XT:", xt)

# st = {1, 2, 3, 4, 5, 5, 1, 3, 6}
# xt=st.copy()
# xt.add(11)
# print("ST:", st)
# print("XT:", xt)

s = {2, 4, 6, 1}
x = {1, 7, 3, 5, 4}
# print(s.difference(x))
# print(s)
# s.difference_update(x)
# print(s)

print(s.isdisjoint(x))
