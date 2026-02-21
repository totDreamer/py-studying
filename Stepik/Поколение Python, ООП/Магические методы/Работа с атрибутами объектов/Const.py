class Const:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError("Удаление атрибута невозможно")


videogame = Const(name="Cuphead")

videogame.developer = "Studio MDHR"
print(videogame.name)
print(videogame.developer)


videogame = Const(name="Disco Elysium")

try:
    videogame.name = "Half-Life: Alyx"
except AttributeError as e:
    print(e)


videogame = Const(name="The Last of Us")

try:
    del videogame.name
except AttributeError as e:
    print(e)
