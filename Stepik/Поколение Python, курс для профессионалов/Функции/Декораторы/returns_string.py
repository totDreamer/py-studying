from functools import wraps

def returns_string(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        val = f(*args, **kwargs)
        if not isinstance(val, str):
            raise TypeError
        return val
    
    return wrapper

@returns_string
def beegeek():
    return 'beegeek'
    
print(beegeek())


@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))