from re import fullmatch


def is_integer(string):
    if fullmatch(r"\-?\d+", string):
        return True
    else:
        return False


print(is_integer("199"))
print(is_integer("-43"))
print(is_integer("5f"))
print(is_integer("5.0"))
print(is_integer("1.1"))
