from functools import wraps


class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not all(map(isinstance, args, self.types)):
                raise TypeError
            return func(*args, **kwargs)

        return wrapper


@type_check([int, int])
def add(a, b):
    return a + b


print(add(1, 2))
print()


@type_check([int, int])
def add(a, b):
    return a + b


try:
    print(add(1, "2"))
except Exception as error:
    print(type(error))
print()


@type_check([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(1, 2))
print()


@type_check([int, int])
def add(a, b, c):
    return a + b + c


print(add(1, 2, 3.0))
