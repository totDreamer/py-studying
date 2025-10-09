from functools import wraps

def square(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)**2
    
    return wrapper

@square
def add(a, b):
    return a + b

print(add(3, 7))



@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)