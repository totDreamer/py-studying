def alternating_sequence(count=None):
    n = 0
    while n != count:
        n += 1
        yield n if n % 2 else -n


generator = alternating_sequence()
print(next(generator))
print(next(generator))

generator = alternating_sequence(10)
print(*generator)