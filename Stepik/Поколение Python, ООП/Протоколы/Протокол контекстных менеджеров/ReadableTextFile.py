class ReadableTextFile:
    def __init__(self, filename):
        self._filename = filename

    def __enter__(self):
        self._obj = open(self._filename, "r", encoding="utf-8")
        return (line.strip() for line in self._obj)

    def __exit__(self, *exc_info):
        self._obj.close()
