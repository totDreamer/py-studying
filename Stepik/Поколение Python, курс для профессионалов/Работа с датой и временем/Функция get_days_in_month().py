from calendar import monthrange, month_name
from datetime import date

def get_days_in_month(year, month):
    year = int(year)
    month = list(month_name).index(month)
    days = [date(year, month, d) for d in range(1, monthrange(year, month)[1] + 1)]
    return days

print(get_days_in_month(2021, 'December'))