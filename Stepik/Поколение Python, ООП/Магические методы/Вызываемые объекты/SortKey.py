class SortKey:
    def __init__(self, *attr):
        self.attr = attr

    def __call__(self, obj):
        return tuple(getattr(obj, a) for a in self.attr)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User({self.name}, {self.age})"


users = [
    User("Gvido", 67),
    User("Timur", 30),
    User("Arthur", 20),
    User("Timur", 45),
    User("Gvido", 60),
]

print(sorted(users, key=SortKey("name")))
print(sorted(users, key=SortKey("name", "age")))
print(sorted(users, key=SortKey("age")))
print(sorted(users, key=SortKey("age", "name")))
