from functools import wraps

def takes(*datatype, **datatypes):
    def takes_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            types = (*datatype, *datatypes.values())
            print(types)
            if not all(isinstance(arg, types) for arg in (*args, *kwargs.values())):
                raise TypeError
            result = f(*args, **kwargs)
            return result
        return wrapper
    return takes_decorator

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))

@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))


# TEST_4:
@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], 3))
except TypeError as e:
    print(type(e))