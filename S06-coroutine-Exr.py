def cen_gen(words):
    print("Start !!!")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * 4

cg=cen_gen(["khar","gav","meymoon","sag","lajan"])
next(cg)
print(cg.send("Ali"))
print(cg.send("khar"))
print(cg.send("saba"))
print(cg.send("sag"))
print(cg.send("lajan"))
print(cg.send("MAJID"))
