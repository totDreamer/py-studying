import sys


class UpperPrint:

    def __enter__(self):
        self._stdout, sys.stdout = sys.stdout, self
        return self

    def __exit__(self, *exc_info):
        sys.stdout = self._stdout

    def write(self, text):
        self._stdout.write(text.upper())



print("Если жизнь одаривает вас лимонами — не делайте лимонад")
print("Заставьте жизнь забрать их обратно!")

with UpperPrint():
    print("Мне не нужны твои проклятые лимоны!")
    print("Что мне с ними делать?")

print("Требуйте встречи с менеджером, отвечающим за жизнь!")
