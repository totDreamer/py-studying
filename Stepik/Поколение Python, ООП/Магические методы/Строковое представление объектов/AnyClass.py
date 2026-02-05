class AnyClass:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self):
        attrbutes = [f"{key}={repr(value)}" for key, value in self.__dict__.items()]
        return f"AnyClass: {', '.join(attrbutes)}"

    def __repr__(self):
        attrbutes = [f"{key}={repr(value)}" for key, value in self.__dict__.items()]
        return f"AnyClass({', '.join(attrbutes)})"


any = AnyClass()

print(str(any))
print(repr(any))


cowboy = AnyClass(name="John", surname="Marston")

print(str(cowboy))
print(repr(cowboy))


obj = AnyClass(
    attr1=10,
    attr2="beegeek",
    attr3=True,
    attr4=[1, 2, 3],
    attr5=("one", "two"),
    attr6=None,
)

print(str(obj))
print(repr(obj))


attrs = {
    "name": "Guido van Rossum",
    "birth_date": "31.01.1956",
    "age": 67,
    "career": "python guru",
}
obj = AnyClass(**attrs)
print(obj.name)
print(obj.birth_date)
print(obj.age)
print(obj.career)
