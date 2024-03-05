year_name = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']


def zodiac(*, year : int):
    return year_name[year % 12]

y = int(input())
print(zodiac(year=y))