def get_weekday(number):
    week = { 1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if number not in range(1, 8):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return week[number]


print(get_weekday(1))

try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
