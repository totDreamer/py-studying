from keyword import iskeyword


class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        if isinstance(value, str) and iskeyword(value):
            raise ValueError("Некорректное значение")
        obj.__dict__[self._attr] = value


class Student:
    name = NonKeyword("name")


student = Student()
student.name = "Peter"

print(student.name)
print()


class Student:
    name = NonKeyword("name")


student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)
print()


class Student:
    name = NonKeyword("name")


student = Student()
student.name = "Peter"

try:
    student.name = "class"
except ValueError as e:
    print(e)
print()


class NonKeywordData:
    obj = NonKeyword("obj")


data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, "Mantrida"]
nonkeyworddata = NonKeywordData()

for item in data:
    nonkeyworddata.obj = item
    print(nonkeyworddata.obj)
print()


class Student:
    name = NonKeyword("name")


print(Student.name.__class__)
