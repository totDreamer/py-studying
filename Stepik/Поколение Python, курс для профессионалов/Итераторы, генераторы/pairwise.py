def pairwise(iterable):
    try:
        iterable = iter(iterable)
        previous = next(iterable)
        for ob in iterable:
            yield (previous, ob)
            previous = ob
        yield (previous, None)
    except StopIteration:
        return iterable

numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))

iterator = iter('stepik')
print(*pairwise(iterator))

print(list(pairwise([])))