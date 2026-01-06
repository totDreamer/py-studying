from re import sub, search

def mult_str(string):
    while search(r'\d+?\(', string):
        string = sub(r'(\d+)\((\w+?)\)', lambda x: x.group(2) * int(x.group(1)), string)
    return string


print(mult_str('hello3(world)hi') == 'helloworldworldworldhi')
print(mult_str('0(s)he0(be)lie0(ve)d') == 'helied')
print(mult_str('bbbb10(2(a))bbb') == 'bbbbaaaaaaaaaaaaaaaaaaaabbb')
print(mult_str('hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd') == 'hiprivdiiidddiiidddiiiddqqprivdiiidddiiidddiiiddqqbqwqdd')
print(mult_str('hhhhhh') == 'hhhhhh')