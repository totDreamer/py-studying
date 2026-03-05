import time


class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = None
        self.min = None
        self.max = None

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, *exc_info):
        self.last_run = time.perf_counter() - self._start
        self.runs.append(self.last_run)
        self.min = min(self.runs)
        self.max = max(self.runs)
