class Versioned:
    def __init__(self):
        self._cache = dict()

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value
        self._cache[obj] = self._cache.get(obj, [])
        self._cache[obj].append(value)

    def get_version(self, obj, n):
        return self._cache[obj][n - 1]

    def set_version(self, obj, n):
        obj.__dict__[self._attr] = self._cache[obj][n - 1]


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19

print(student.age)
print()


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))
print()


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
Student.age.set_version(student, 1)
print(student.age)
print()


class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 2)
print(student1.age)
print(student2.age)
print()


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)

Student.age.set_version(student, 1)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

Student.age.set_version(student, 2)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))
print()


class Student:
    age = Versioned()


print(Student.age.__class__)
print()


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
Student.age.set_version(student, 1)
student.age = 20
student.age = 21

print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))
print(Student.age.get_version(student, 4))
