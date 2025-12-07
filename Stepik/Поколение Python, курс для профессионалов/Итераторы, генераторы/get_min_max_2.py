def get_min_max(iterable):
    max_value = None
    min_value = None
    
    for i in iterable:
        if max_value is None or i > max_value:
            max_value = i
        if min_value is None or i < min_value:
            min_value = i
    
    if max_value is None:
        return None
    
    return (min_value, max_value)


iterable = iter(range(10))

print(get_min_max(iterable))


iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

iterable = iter([])

print(get_min_max(iterable))