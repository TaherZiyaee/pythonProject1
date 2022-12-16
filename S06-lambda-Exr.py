# ----------------- 1 ------------------
# li = [3, -43, 54, 11, -3, 76, 34, -6, 19, 53, -38]
# print('list:', li)
# odd = list(filter(lambda x: x % 2 != 0, li))
# even = list(filter(lambda x: x % 2 == 0, li))
# print('odd:', odd, '\nlen odd:', len(odd))
# print('even:', even, '\nlen even:', len(even))

# ----------------- 2 ------------------
# lst = [('taher', 37), ('masoud', 31), ('hossein', 36), ('jafar', 81), ('noyan', 6)]
# print('list:', lst)
# lst.sort(key=lambda x: x[1])
# print('sorted list:', lst)

# ----------------- 3 ------------------
# lst = [{'name': 'Apple', 'Weight': 50, 'color': 'red'},
#        {'name': 'Orange', 'Weight': 67, 'color': 'orange'},
#        {'name': 'Cherry', 'Weight': 25, 'color': 'black'},
#        {'name': 'Watermeloan', 'Weight': 120, 'color': 'green'}]
# print('list:', lst)
# lst.sort(key=lambda x: x['color'])
# print('sorted list:', lst)

# ----------------- 4 ------------------
# li = [3, -43, 54, 11, -3, 76, 34, -6, 19, 53, -38]
# print('list:', li)
# odd = list(filter(lambda x: x % 2 != 0, li))
# even = list(filter(lambda x: x % 2 == 0, li))
# print('odd:', odd)
# print('even:', even)

# ----------------- 5 ------------------
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('List:', lst)
# square = list(map(lambda x: x ** 2, lst))
# cube = list(map(lambda x: x ** 3, lst))
# print('Square:', square)
# print('Cube:', cube)

# ----------------- 6 ------------------
# s = 'taher'
# c = 't'
# result = lambda x, y: True if x.startswith(y) else False
# print(result(s, c))

# ----------------- 7 ------------------
# is_num = lambda x: x.replace('.', '', 1).isdigit()
# print(is_num('3.5'))
# print(is_num('afsd.gf'))
# print(is_num('11'))
# print(is_num('2.8a'))

