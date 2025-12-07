def with_previous(iterable):
    previous = None
    for ob in iterable:
        yield (ob, previous)
        previous = ob

numbers = [1, 2, 3, 4, 5]
print(*with_previous(numbers))

iterator = iter('stepik')
print(*with_previous(iterator))