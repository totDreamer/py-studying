from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(object):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def _from_int(object):
        print(f"Целое число: {object}")

    @format.register(float)
    @staticmethod
    def _from_float(object):
        print(f"Вещественное число: {object}")

    @format.register(tuple)
    @staticmethod
    def _from_tuple(object):
        print(f"Элементы кортежа: {', '.join(map(str, object))}")

    @format.register(list)
    @staticmethod
    def _from_list(object):
        print(f"Элементы списка: {', '.join(map(str, object))}")

    @format.register(dict)
    @staticmethod
    def _from_dict(object):
        print(f"Пары словаря: {', '.join(map(str, object.items()))}")


Formatter.format(1337)
Formatter.format(20.77)

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

Formatter.format({"Cuphead": 1, "Mugman": 3})
Formatter.format({1: "one", 2: "two"})
Formatter.format({1: True, 0: False})

try:
    Formatter.format("All them years, Dutch, for this snake?")
except TypeError as e:
    print(e)
