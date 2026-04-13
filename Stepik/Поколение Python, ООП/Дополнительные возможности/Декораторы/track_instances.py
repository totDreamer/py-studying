from functools import wraps


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @wraps(old_init)
    def new_init(*args, **kwargs):
        old_init(*args, **kwargs)
        cls.instances.append(args[0])

    cls.__init__ = new_init
    return cls


@track_instances
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name!r})"


obj1 = Person("object 1")
obj2 = Person("object 2")

print(Person.instances)
