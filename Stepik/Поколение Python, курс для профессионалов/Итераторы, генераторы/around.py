def around(iterable):
    try:
        iterable = iter(iterable)
        previous = None
        current = next(iterable)
        for ob in iterable:
            yield (previous, current, ob)
            previous, current = current, ob
        yield (previous, current, None)
    except StopIteration:
        return iterable

numbers = [1, 2, 3, 4, 5]
print(*around(numbers))

iterator = iter('hey')
print(*around(iterator))