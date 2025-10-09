from functools import wraps

def repeat(times):
    def repeat_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(times-1):
                f(*args, **kwargs)
            return f(*args, **kwargs)
        return wrapper
    return repeat_decorator

@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
say_beegeek()



@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
print(say_beegeek.__name__)
print(say_beegeek.__doc__)