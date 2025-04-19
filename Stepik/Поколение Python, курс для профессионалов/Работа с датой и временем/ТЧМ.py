from datetime import date, timedelta

def third_thursday(year):
    y = int(year)
    all_t_t = []

    for m in range(1, 13):
        d = date(y, m, 1)
        days_utill_t = (3 - d.weekday()) % 7
        third_t = (d + timedelta(days=days_utill_t)) + timedelta(days=14)
        all_t_t.append(third_t.strftime('%d.%m.%Y'))

    return all_t_t


print(*third_thursday(input()), sep='\n')