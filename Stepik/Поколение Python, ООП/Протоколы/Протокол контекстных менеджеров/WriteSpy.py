class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self._file_1 = file1
        self._file_2 = file2
        self._to_close = to_close

    def write(self, text):
        try:
            if not self.writable():
                raise ValueError("Файл закрыт или недоступен для записи")
            self._file_1.write(text)
            self._file_2.write(text)
        except Exception:
            raise ValueError("Файл закрыт или недоступен для записи")

    def close(self):
        self._file_1.close()
        self._file_2.close()

    def writable(self):
        try:
            return self._file_1.writable() and self._file_2.writable()
        except ValueError:
            return False

    def closed(self):
        return self._file_1.closed and self._file_2.closed

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        if self._to_close:
            self.close()
