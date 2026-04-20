from functools import wraps


class Predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        return Predicate(lambda *a, **kw: self(*a, **kw) and other(*a, **kw))

    def __or__(self, other):
        return Predicate(lambda *a, **kw: self(*a, **kw) or other(*a, **kw))

    def __invert__(self):
        return Predicate(lambda *a, **kw: not self(*a, **kw))


def predicate(func):
    return wraps(func)(Predicate(func))
