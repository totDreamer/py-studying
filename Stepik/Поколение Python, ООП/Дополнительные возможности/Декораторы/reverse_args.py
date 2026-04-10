from functools import update_wrapper


class reverse_args:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)


@reverse_args
def power(a, n):
    return a**n


print(power(2, 3))
print()


@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat("apple", "cherry", "melon"))
