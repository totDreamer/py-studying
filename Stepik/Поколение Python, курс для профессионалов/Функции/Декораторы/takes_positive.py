def takes_positive(f):
    def wrapper(*args, **kwargs):
        values = [*args, *kwargs.values()]
        total = 0
        for v in values:
            if not isinstance(v, int):
                raise TypeError
            if v <= 0:
                raise ValueError
            total += v
        return total
    
    return wrapper

@takes_positive
def positive_sum(*args):
    return sum(args)
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))


@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))