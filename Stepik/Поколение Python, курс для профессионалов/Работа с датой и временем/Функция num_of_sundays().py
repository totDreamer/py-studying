import datetime

def num_of_sundays(year):
    sundays = 0
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date = datetime.date(year, month, day)
                if date.weekday() == 6:
                    sundays += 1
            except ValueError:
                break
    return sundays

print(num_of_sundays(2025))
