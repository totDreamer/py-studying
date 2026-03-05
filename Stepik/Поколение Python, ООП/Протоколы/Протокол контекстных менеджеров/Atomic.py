from copy import copy, deepcopy


class Atomic:
    def __init__(self, data, deep=False):
        self._data = data
        self._backup = deepcopy(data) if deep else copy(data)

    def __enter__(self):
        return self._backup

    def __exit__(self, exc_type, exc_value, traceback):
        if not exc_value:
            if isinstance(self._data, list):
                self._data[:] = self._backup
            elif isinstance(self._data, (set, dict)):
                self._data.clear()
                self._data.update(self._backup)
        return True
