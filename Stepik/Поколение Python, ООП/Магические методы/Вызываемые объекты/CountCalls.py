class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)


@CountCalls
def add(a, b):
    return a + b


print(add(1, 2))
print(add(2, 3))
print(add.calls)


@CountCalls
def square(a):
    return a**2


for i in range(100):
    square(i)

print(square.calls)
