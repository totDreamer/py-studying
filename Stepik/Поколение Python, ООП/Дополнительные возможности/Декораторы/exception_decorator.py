from functools import update_wrapper


class exception_decorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return (self.func(*args, **kwargs), None)
        except Exception as e:
            return (None, type(e))


@exception_decorator
def func(x):
    return 2 * x + 1


print(func(1))
print(func("bee"))
print()


@exception_decorator
def f(x, y):
    return x * y


print(f("stepik", 10))
