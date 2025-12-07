def unique(iterable):
    unique_val = set()
    for ob in iterable:
            if isinstance(ob, (list, tuple, dict)):
                unique(ob)
            
            if ob not in unique_val:
                unique_val.add(ob)
                yield ob

numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))

iterator = iter('111222333')
uniques = unique(iterator)
print(next(uniques))
print(next(uniques))
print(next(uniques))