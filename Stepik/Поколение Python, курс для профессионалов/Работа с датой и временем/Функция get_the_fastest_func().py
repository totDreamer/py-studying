import time
from math import factorial

def get_the_fastest_func(funcs, arg):
    minimal_time = 10000000000
    fastest_func = None
    for func in funcs:
        start_time = time.monotonic()
        func(arg)
        end_time = time.monotonic()
        time_result = end_time - start_time
        if time_result < minimal_time:
            minimal_time = time_result
            fastest_func = func
    return fastest_func
