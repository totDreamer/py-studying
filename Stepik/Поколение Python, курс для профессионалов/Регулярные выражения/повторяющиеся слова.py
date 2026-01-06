from re import sub


def repit_w(string):
    return sub(r"\b(\w+)\b(\W*?\1\W*?)+\b", r"\1", string)


print(repit_w(input()))
print(repit_w("beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik"))
print(repit_w("hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!"))
print(repit_w("wow Wow wow WOW"))
