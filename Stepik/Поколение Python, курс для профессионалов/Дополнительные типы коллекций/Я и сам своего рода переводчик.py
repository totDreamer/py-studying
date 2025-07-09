import string

def magic_translate(sym_str, word):
    eng_chars = string.ascii_lowercase
    magic_dict = str.maketrans(eng_chars, sym_str)
    magic_word = word.lower().translate(magic_dict)
    return magic_word

#s_str = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩'
#w = 'I love Python =)'
#print(magic_translate(s_str, w))
#s_str = '😀😄😁😆😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨😫😩🥺😢😭😤😠😡'
#w = 'Dont be so sad!'
#print(magic_translate(s_str, w))
s_str, w = input(), input()
print(magic_translate(s_str, w))
