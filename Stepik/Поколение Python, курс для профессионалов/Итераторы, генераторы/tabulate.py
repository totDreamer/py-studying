from itertools import count

def tabulate(func):
    c_args = count(1)
    while True:
        yield func(next(c_args))

func = lambda x: x
values = tabulate(func)
print(next(values))
print(next(values))

func = lambda x: x + 10
values = tabulate(func)
print(next(values))
print(next(values))
print(next(values))

func = lambda x: x ** 2
values = tabulate(func)
for _ in range(100):
    print(next(values))

def func(n):
    return 'beegeek' * n
values = tabulate(func)
for _ in range(10):
    print(next(values))