def flatten(nested_list):
    for l in nested_list:
        if isinstance(l, int): 
            yield l
        else:
            yield from flatten(l)


generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)

generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)