from json import dumps


class JsonSerializableMixin:
    def to_json(self):
        return dumps(self.__dict__)


class Empty(JsonSerializableMixin):
    pass


obj = Empty()
print(obj.to_json())
print()


class Triangle(JsonSerializableMixin):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


triangle = Triangle(3, 5, 4)
print(triangle.to_json())
