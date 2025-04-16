from datetime import datetime, timedelta

def choose_plural(amount, declensions):
    suffixes = {0: 2, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2}
    if amount % 100 in (11, 12, 13, 14):
        return declensions[2]
    else:
        return declensions[suffixes.get(amount % 10)]
    
d_decl = ('день', 'дня', 'дней')
h_decl = ('час', 'часа', 'часов')
m_decl = ('минута', 'минуты', 'минут')
    
def time_until(date):
    pattern = '%d.%m.%Y %H:%M'
    release = datetime.strptime('08.11.2022 12:00', pattern)
    date = datetime.strptime(date, pattern)

    if date >= release:
        return 'Курс уже вышел!'

    result = release - date
    days = result.days
    hours = int(result.total_seconds() // 3600 % 24)
    minutes = int(result.total_seconds() // 60 % 60)

    if days and hours:
        return f'До выхода курса осталось: {days} {choose_plural(days, d_decl)} и {hours} {choose_plural(hours, h_decl)}'
    
    elif days:
        return f'До выхода курса осталось: {days} {choose_plural(days, d_decl)}'
    
    elif hours and minutes:
        return f'До выхода курса осталось: {hours} {choose_plural(hours, h_decl)} и {minutes} {choose_plural(minutes, m_decl)}'
    
    elif hours:
        return f'До выхода курса осталось: {hours} {choose_plural(hours, h_decl)}'
    
    else:
        return f'До выхода курса осталось: {minutes} {choose_plural(minutes, m_decl)}'

print(time_until(input()))