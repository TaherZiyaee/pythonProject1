import mod1

print(mod1.func1(3))
print(mod1.func2("Taher"))

f1 = mod1.func1
print(f1(2))

#------------------------

from pkg1.mod2 import func3,func4

func3(3)
func4("SARA")
func3(2)

from mod1 import *
print(func1(2))
print(func2("Jafar"))