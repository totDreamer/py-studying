from re import fullmatch


def is_fraction(string):
    if fullmatch(r"\-?\d+/0*[1-9]\d*", string):
        return True
    else:
        return False


print(is_fraction("1000/1"))
print(is_fraction("-54/9"))
print(is_fraction("71"))
print(is_fraction("1/0"))
print(is_fraction(""))
print(is_fraction("54365486548645/472342935648904709456"))
print(is_fraction("1000/00001"))
print(is_fraction("-1000/00001"))
