from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if self.validate(value):
            obj.__dict__[self._attr] = value

    def __delete__(self, obj):
        del obj.__dict__[self._attr]

    @abstractmethod
    def validate(self):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):
        if not isinstance(obj, (int, float)):
            raise TypeError("Устанавливаемое значение должно быть числом")
        elif self.minvalue is not None and obj < self.minvalue:
            raise ValueError(
                f"Устанавливаемое число должно быть больше или равно {self.minvalue}"
            )
        elif self.maxvalue is not None and obj > self.maxvalue:
            raise ValueError(
                f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}"
            )
        return True


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        elif self.minsize is not None and len(obj) < self.minsize:
            raise ValueError(
                f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}"
            )
        elif self.maxsize is not None and len(obj) > self.maxsize:
            raise ValueError(
                f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}"
            )
        elif self.predicate is not None and not self.predicate(obj):
            raise ValueError(
                "Устанавливаемая строка не удовлетворяет дополнительным условиям"
            )
        return True


class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)
print()


class Student:
    age = Number(18, 99)


try:
    student = Student()
    student.age = "19"
except TypeError as error:
    print(error)
print()


class Student:
    age = Number(18, 99)


try:
    student = Student()
    student.age = 16
except ValueError as error:
    print(error)
print()


class Student:
    age = Number(18, 99)


try:
    student = Student()
    student.age = 101
except ValueError as error:
    print(error)
print()


class PositiveNumber:
    num = Number(0)


positivenumber = PositiveNumber()
positivenumber.num = 0
print(positivenumber.num)

try:
    positivenumber.num = -1
except ValueError as e:
    print(e)
print()


class Student:
    age = Number(18, 99)


student = Student()
try:
    print(student.age)
except AttributeError as e:
    print(e)
print()


class Student:
    age = Number(18, 99)


print(Student.age.__class__)
