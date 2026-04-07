from abc import ABC, abstractmethod


class Family(ABC):
    def __init__(self, mood=None):
        self.mood = mood if mood is not None else "neutral"

    @abstractmethod
    def greet(self):
        pass


class Father(Family):
    def greet(self):
        return "Hello!"

    def be_strict(self):
        self.mood = "strict"


class Mother(Family):
    def greet(self):
        return "Hi, honey!"

    def be_kind(self):
        self.mood = "kind"


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass


father = Father()
mother = Mother()

print(father.mood)
print(mother.mood)
print(father.greet())
print(mother.greet())
print()


father = Father("happy")
mother = Mother("unhappy")

print(father.mood)
print(mother.mood)
father.be_strict()
mother.be_kind()
print(father.mood)
print(mother.mood)
print()


daughter = Daughter()

print(daughter.greet())
print(daughter.mood)
daughter.be_kind()
print(daughter.mood)
daughter.be_strict()
print(daughter.mood)
print()


son = Son()

print(son.greet())
print(son.mood)
son.be_kind()
print(son.mood)
son.be_strict()
print(son.mood)
