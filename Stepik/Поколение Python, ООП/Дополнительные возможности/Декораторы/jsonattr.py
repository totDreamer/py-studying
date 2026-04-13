from json import load


def jsonattr(filename):
    def wrapper(cls):
        with open(filename, "r", encoding="UTF-8") as f:
            for attr, value in load(f).items():
                setattr(cls, attr, value)
            return cls

    return wrapper


with open("test.json", "w") as file:
    file.write('{"x": 1, "y": 2}')


@jsonattr("test.json")
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)
