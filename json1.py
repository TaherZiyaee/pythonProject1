# d = {"name":"Taher",
#      "family":"Ziaei",
#      "age":37,
#      "marks":[17,20,19]
#      }
#
# print(d["name"])

# import json

# jn_str = "3.6"
# jn_str = '"Taher"'
# jn_str = "[1,2,3,4]"
# jn_str = '{"a": 1, "b": 2}'
# jn_str = '{"A","B","C","D","B"}'
# py_type = json.loads(jn_str)
#
# print(jn_str, "\n", type(jn_str))
# print(40 * "-")
# print(py_type, "\n", type(py_type))

# import json
#
# with open("myfile1.json","r") as jf:
#     s = json.load(jf)
#
# print(s)
# print(type(s))

# import json
# d = {"a": 1, "b": 2}
# j=json.dumps(d)
# print(j)
# print(type(j))

import json
d = {"name":"Taher",
     "family":"Ziaei",
     "age":37,
     "marks":{"math":[17,20,19],"physic":[12,18,9]},
     "lessons":["math","physic","sport","english language"]
     }
with open("myfile1.json", "w") as jf:
    json.dump(d, jf,indent=4,sort_keys=True,separators=(",",":"))
