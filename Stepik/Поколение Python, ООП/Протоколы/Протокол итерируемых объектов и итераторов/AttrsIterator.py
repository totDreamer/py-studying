class AttrsIterator:
    def __init__(self, obj):
        self.obj = ((key, value) for key, value in obj.__dict__.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.obj)


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User("Debbie", "Harry", 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)


class Kemal:
    def __init__(self):
        self.family = "cats"
        self.breed = "british"
        self.master = "Kemal"


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))
