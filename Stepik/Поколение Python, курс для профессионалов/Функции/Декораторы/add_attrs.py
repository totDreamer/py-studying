from functools import wraps

def add_attrs(**kwattrs):
    def add_attrs_dec(f):
        for attr, value in kwattrs.items():
            setattr(f, attr, value)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return add_attrs_dec


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'
    
print(beegeek.attr1)
print(beegeek.attr2)



@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'
    
print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)