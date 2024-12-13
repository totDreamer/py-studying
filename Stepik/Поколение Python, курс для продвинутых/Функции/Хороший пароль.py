def pass_check(password):
    result = ''
    if (any(char.isdigit() for char in password) and
        any(char.islower() for char in password) and
        any(char.isupper() for char in password) and
        len(password) >= 7):
        result = 'YES'
    else:
        result = 'NO'
    return result

print(pass_check('abcABC9'))  # Должно вернуть YES
print(pass_check('abAB34'))   # Должно вернуть NO
print(pass_check('DFSDFSDFSDsdfjsdfnsm'))  # Должно вернуть NO
