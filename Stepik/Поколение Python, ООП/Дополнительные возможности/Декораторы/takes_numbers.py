from functools import update_wrapper


class takes_numbers:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if not all(
            map(lambda v: isinstance(v, (int, float)), (*args, *kwargs.values()))
        ):
            raise TypeError("Аргументы должны принадлежать типам int или float")
        return self.func(*args, **kwargs)


@takes_numbers
def mul(a, b):
    return a * b


print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))
print()


@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul(1, "2"))
except TypeError as error:
    print(error)
print()


@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul("1", 2))
except TypeError as error:
    print(error)
print()


@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul("1", "2"))
except TypeError as error:
    print(error)
print()


@takes_numbers
def mul(a, b=2):
    return a * b


try:
    print(mul(1, b="2"))
except TypeError as error:
    print(error)
print()


@takes_numbers
def mul(a, b=2):
    """multiplication"""
    return a * b


print(mul.__name__)
print(mul.__doc__)
print(mul(3, 4))
