class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + " " + self.surname

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)


person = Person("Меган", "Фокс")

print(person.name)
print(person.surname)
print(person.fullname)


person = Person("Меган", "Фокс")

person.name = "Стефани"
print(person.fullname)


person = Person("Алан", "Тьюринг")

person.surname = "Вирт"
print(person.fullname)


person = Person("Джон", "Маккарти")

person.fullname = "Алан Тьюринг"
print(person.name)
print(person.surname)
