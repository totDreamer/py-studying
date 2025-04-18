import time

def calculate_it(func, *args):
    time_start = time.monotonic()
    result = func(*args)
    time_end = time.monotonic()
    time_result = time_end - time_start
    return (result, time_result)


def add(a, b, c):
    time.sleep(3)
    return a + b + c
print(calculate_it(add, 1, 2, 3))