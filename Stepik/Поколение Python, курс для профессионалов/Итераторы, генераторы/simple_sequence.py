def simple_sequence():
    start = 1
    while True:
        for _ in range(start):
            yield start
        start += 1

generator = simple_sequence()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]
print(*numbers)