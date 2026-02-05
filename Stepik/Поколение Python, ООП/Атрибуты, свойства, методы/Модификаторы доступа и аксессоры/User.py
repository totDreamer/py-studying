class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError("Некорректное имя")
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if not isinstance(age, int) or not 0 <= age <= 110:
            raise ValueError("Некорректный возраст")
        self._age = age


user = User("Гвидо", 67)

print(user.get_name())
print(user.get_age())


user = User("Гвидо", 67)

user.set_name("Тимур")
user.set_age(30)

print(user.get_name())
print(user.get_age())


user = User("Меган", 37)

invalid_names = (-1, True, "", [], "123456", "Меган906090")

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)
