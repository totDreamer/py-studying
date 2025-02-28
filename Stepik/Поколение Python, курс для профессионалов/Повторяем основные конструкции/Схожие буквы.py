def sym_lang(*args):
    sym_lang = []
    for arg in args:
        sym_lang.append('en' if 64 < ord(arg) < 123 else 'ru')
    if 'ru' in sym_lang and 'en' in sym_lang:
        return 'mix'
    else:
        return sym_lang[0]

a, b, c = input(), input(), input()
print(sym_lang(a, b, c))