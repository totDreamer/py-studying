from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(obj):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_int_float(obj):
        return obj * 2

    @process.register(str)
    @staticmethod
    def _from_str(obj):
        return obj.upper()

    @process.register(list)
    @staticmethod
    def _from_list(obj):
        return sorted(obj)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(obj):
        return tuple(sorted(obj))


print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process("hello"))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))


try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)
