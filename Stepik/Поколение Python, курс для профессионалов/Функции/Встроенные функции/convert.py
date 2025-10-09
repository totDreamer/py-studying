def convert(number):
    if number >= 0:
        return (bin(number)[2:], oct(number)[2:], hex(number)[2:].upper())
    else:
        return ('-' + bin(number)[3:], '-' + oct(number)[3:], '-' + hex(number)[3:].upper())


print(convert(15))
print(convert(-24))