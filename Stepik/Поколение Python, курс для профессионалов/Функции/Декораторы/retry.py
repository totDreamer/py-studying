from functools import wraps

class MaxRetriesException(Exception):
    pass

def retry(times):
    def retry_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return f(*args, **kwargs)
                except:
                    continue
            raise MaxRetriesException
        return wrapper
    return retry_decorator

@retry(3)
def no_way():
    raise ValueError
   
try:
    no_way()
except Exception as e:
    print(type(e))



@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')
    
beegeek()