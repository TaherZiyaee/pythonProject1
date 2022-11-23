# Ramznegari
def encryptor_(mypass):
    pass_ = mypass
    textCrypted = ''
    for c in pass_:
        x = ord(c) + 4 * 3
        textCrypted += chr(x)
    return textCrypted

print(encryptor_('taher zia'))
#--------------------------------

# def f(x):
#     return 2*x+1
# print(f(-2))
