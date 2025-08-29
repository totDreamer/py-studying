def is_power(number):
    if number < 1:
        return False
    if number == 1:
        return True
    return is_power(number/2)

print(is_power(512))
print(is_power(15))
print(is_power(1))