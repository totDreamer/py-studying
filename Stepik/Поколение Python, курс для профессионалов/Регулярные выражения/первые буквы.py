from re import sub


def first_chars(string):
    return sub(r"\b(\w)(\w)", r"\2\1", string)


print(first_chars(input()))
print(first_chars("This is Python"))
print(first_chars("Hi, everyone. Lets start a lesson!"))
