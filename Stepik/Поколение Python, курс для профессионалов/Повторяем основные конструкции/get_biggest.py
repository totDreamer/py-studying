def get_biggest(numbers):
    if not numbers:
        return -1
    max_len = len(str(max(numbers)))
    numbers = sorted(numbers, key=lambda x: str(x) * max_len, reverse=True)
    result = int(''.join(map(str, numbers)))
    return result

print(get_biggest([100, 2, 3452]))


print(get_biggest([7, 71, 72]) == 77271)
print(get_biggest([0, 0, 0, 0, 0, 0]) == 0)
print(get_biggest([]) == -1)
print(get_biggest([72, 7274]) == 727472)
print(get_biggest([62, 626]) == 62662)
print(get_biggest([953, 9534]) == 9539534)
print(get_biggest([262, 26]) == 26262)

print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]) == 78554656558534233433222211311)