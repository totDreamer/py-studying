from itertools import chain


_sentinel = object()


class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self._first = next(self.iterable, _sentinel)
        if self._first is not _sentinel:
            self.iterable = chain([self._first], self.iterable)
        self._last = _sentinel
        self._buffer_last = _sentinel
        self._accesses = 0
        self._empty_accesses = 0
        self._empty_flag = False

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first is _sentinel:
            raise AttributeError("Исходный итерируемый объект пуст")
        return self._first

    @property
    def last(self):
        if self._last is _sentinel:
            raise AttributeError("Последнего элемента нет")
        return self._last

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_elem = next(self.iterable)
            self._last = next_elem
            self._accesses += 1
            self._buffer_last = next(self.iterable, _sentinel)
            if self._buffer_last is not _sentinel:
                self.iterable = chain([self._buffer_last], self.iterable)
            else:
                self._empty_flag = True
            return next_elem
        except StopIteration:
            self._empty_accesses += 1
            self._empty = True
            raise

    def is_empty(self):
        return self._empty_flag


loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(list(loop_tracker))
print()

loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)
print()


loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)
print()


loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
