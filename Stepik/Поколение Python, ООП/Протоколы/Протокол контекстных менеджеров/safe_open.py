from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode="r"):
    try:
        file = open(filename, mode)
        yield (file, None)
        file.close()
    except Exception as exp:
        yield (None, exp)
