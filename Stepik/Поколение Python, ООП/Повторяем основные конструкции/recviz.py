from functools import wraps


def recviz(func, count=-1):
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        args_list = ", ".join(repr(arg) for arg in args)
        if kwargs:
            args_list += ", " + (", ".join([f"{k}={repr(w)}" for k, w in kwargs.items()]))
        whitespace = "    " * count

        print(f"{whitespace}-> {func.__name__}({args_list})")
        result = func(*args, **kwargs)
        print(f"{whitespace}<- {repr(result)}")
        count -= 1
        return result

    return wrapper


@recviz
def add(a, b):
    return a + b


add(1, b=2)


@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(4)


@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)


@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)


add("a", b="b", c="c", d=3, e=True)
