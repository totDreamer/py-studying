def reverse_args(f):
    def wrapper(*args, **kwargs):
        return f(*args[::-1], **kwargs)
    
    return wrapper

@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))


@reverse_args
def operation(a, b, name):
    return a // b + name
    
print(operation(10, 90, name=1))