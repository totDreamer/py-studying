from datetime import date, timedelta

def years_days(year):
    start = date(year, 1, 1)
    while start.year != year + 1:
        yield start
        start += timedelta(1)

print(years_days(2022))

dates = years_days(2025)
print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))