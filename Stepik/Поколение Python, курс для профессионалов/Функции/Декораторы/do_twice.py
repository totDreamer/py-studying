def do_twice(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return f(*args, **kwargs)
        
    return wrapper

@do_twice
def beegeek():
    print('beegeek')
    
beegeek()


@do_twice
def beegeek():
    print('beegeek')
    
print(beegeek())


@do_twice
def beegeek():
    return 'beegeek'
    
print(beegeek())