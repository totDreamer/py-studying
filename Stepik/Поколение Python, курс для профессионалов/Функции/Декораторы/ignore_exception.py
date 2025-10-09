from functools import wraps

def ignore_exception(*types):
    def ignore_exception_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except types as err:
                print(f'Исключение {type(err).__name__} обработано')
            except Exception as err:
                raise err
        return wrapper
    return ignore_exception_decorator

@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x
    
f(0)


min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))

