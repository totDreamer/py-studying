from functools import wraps


class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if type(e) in self.exceptions:
                    print(f"Исключение {e.__class__.__name__} обработано")
                else:
                    raise

        return wrapper


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x


func(0)
print()


min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, "2", 3, [4, 5]))
except Exception as error:
    print(type(error))
