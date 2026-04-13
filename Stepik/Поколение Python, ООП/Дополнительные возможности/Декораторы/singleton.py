from functools import wraps


def singleton(cls):
    cls._instance = None

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    cls.__new__ = wrapper
    return cls


@singleton
class MyClass:
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)
