from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    file = open(filename, "a+", encoding="utf-8")
    file.seek(0)
    backup = file.read()

    try:
        yield file
    except Exception as exp:
        file.truncate(0)
        file.write(backup)
        print(f"Во время записи в файл было возбуждено исключение {type(exp).__name__}")
    finally:
        file.close()


with safe_write("undertale.txt") as file:
    file.write("Тень от руин нависает над вами, наполняя вас решительностью")

with open("undertale.txt") as file:
    print(file.read())
