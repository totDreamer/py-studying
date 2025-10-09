from functools import wraps

def trace(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        val = f(*args, **kwargs)
        print(f'TRACE: вызов {f.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {f.__name__}(): {repr(val)}')
        return val
    
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'
    
say('Jane', 'Hello, World')


@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c
    
print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)