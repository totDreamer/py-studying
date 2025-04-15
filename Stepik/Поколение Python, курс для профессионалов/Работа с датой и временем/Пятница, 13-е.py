from datetime import datetime, date

weekday_13 = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}

def day_13(year):
    for month in range(1, 13):
            try:
                day = 13
                d = date(year, month, day)
                weekday_13[d.weekday()] += 1
            except ValueError:
                break

for year in range(1, 10000):
    day_13(year)

print(*weekday_13.values(), sep='\n')