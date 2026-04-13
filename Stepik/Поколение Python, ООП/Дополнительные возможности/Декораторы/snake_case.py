import re


def snake_case(attrs: bool = False):
    def to_snake(name: str) -> str:
        s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
        s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
        return s2.lower()

    def decorator(cls):
        items = list(cls.__dict__.items())

        for name, value in items:
            if name.startswith("__") and name.endswith("__"):
                continue

            if not callable(value) and not attrs:
                continue

            prefix = ""
            core = name

            while core.startswith("_") and not core.startswith("__"):
                prefix += "_"
                core = core[1:]

            new_name = prefix + to_snake(core)

            if new_name != name:
                setattr(cls, new_name, value)
                delattr(cls, name)

        return cls

    return decorator


@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())
print()


@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2


print(MyClass.first_attr)
print(MyClass.super_second_attr)
print()


@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()

print(MyClass.FirstAttr)
print(obj.first_method())
