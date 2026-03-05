class Suppress:
    def __init__(self, *exceptions):
        self._exceptions = exceptions
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, self._exceptions):
            self.exception = exc_value
            return True
        return False


with Suppress(NameError):
    print("Этой переменной не существует -->", variable)

print("Завершение программы")
