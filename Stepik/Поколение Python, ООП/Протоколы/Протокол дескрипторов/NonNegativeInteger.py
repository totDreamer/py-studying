class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        if self._default is None:
            raise AttributeError("Атрибут не найден")
        return self._default

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError("Некорректное значение")


class Student:
    score = NonNegativeInteger("score")


student = Student()
student.score = 90

print(student.score)
print()


class Student:
    score = NonNegativeInteger("score", 0)


student = Student()

print(student.score)
student.score = 0
print(student.score)
print()


class Student:
    score = NonNegativeInteger("score")


student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)
print()


class Student:
    score = NonNegativeInteger("score")


student = Student()

try:
    student.score = -90
except ValueError as e:
    print(e)
