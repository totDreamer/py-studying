from datetime import date, timedelta

def dates(start: date, count=None) -> GeneratorExit:
    while not count:
        try:
            yield start
            start += timedelta(1)
        except:
            break
    while count:
        yield start
        start += timedelta(1)
        count -= 1


generator = dates(date(2022, 3, 8))
print(next(generator))
print(next(generator))
print(next(generator))


generator = dates(date(2022, 3, 8), 5)
print(*generator)


generator = dates(date(9999, 1, 7))
for _ in range(348):
    next(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
try:
   print(next(generator))
except StopIteration:
    print('Error')