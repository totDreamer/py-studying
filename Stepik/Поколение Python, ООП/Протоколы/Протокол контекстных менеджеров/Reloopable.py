class Reloopable:
    def __init__(self, file):
        self._file = file

    def __enter__(self):
        return list(map(str.strip, self._file))
    
    def __exit__(self, *exc_info):    
        self._file.close()