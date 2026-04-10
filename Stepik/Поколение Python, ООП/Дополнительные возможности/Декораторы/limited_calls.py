from functools import wraps


class MaxCallsException(Exception):
    def __str__(self):
        return "Превышено допустимое количество вызовов"


class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.n == 0:
                raise MaxCallsException
            self.n -= 1
            return func(*args, **kwargs)

        return wrapper


@limited_calls(3)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)
