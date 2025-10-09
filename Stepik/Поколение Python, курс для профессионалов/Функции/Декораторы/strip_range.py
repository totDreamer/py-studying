from functools import wraps

def strip_range(start: int, end: int, char: str = '.'):
    def strip_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            nonlocal end
            val = f(*args, **kwargs)
            if end >  len(val):
                end = len(val)
            return val[:start] + char*(end - start) + val[end:]
        return wrapper
    return strip_decorator

@strip_range(3, 5)
def beegeek():
    return 'beegeek'
    
print(beegeek())


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'
    
print(beegeek())

@strip_range(20, 30)
def beegeek():
    return 'beegeek'
    
print(beegeek())