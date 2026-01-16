from re import fullmatch


def is_decimal(string):
    if fullmatch(r"\-?\d*\.\d+|\-?\d+\.?", string):
        return True
    else:
        return False


print(is_decimal("100"))
print(is_decimal("199.1"))
print(is_decimal("-0.2"))
print(is_decimal(".-95"))
print(is_decimal("-.95"))
print(is_decimal(".10"))
print(is_decimal("1-1"))

strings = ["100.", "349..", "-425.", "-1248.."]
for string in strings:
    print(is_decimal(string))
