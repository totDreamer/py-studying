from functools import wraps

def prefix(string, to_the_end=False):
    def prefix_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return f(*args, **kwargs) + string
            else:
                return string + f(*args, **kwargs)
        return wrapper
    return prefix_decorator

@prefix('€')
def get_bonus():
    return '2000'
    
print(get_bonus())


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
       
print(get_bonus())