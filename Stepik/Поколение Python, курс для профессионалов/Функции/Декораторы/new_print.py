def new_print(f):
    def wrapper(*args, **kwargs):
        args = [str(arg).upper() for arg in args]
        kwargs = {key: str(value).upper() for key, value in kwargs.items()}
        upper_value = f(*args, **kwargs)
        return upper_value
    return wrapper

print = new_print(print)

print('hi', 'there', end='!')
print('are you in trouble?')
print(111, 222, 333, sep='xxx')