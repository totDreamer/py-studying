from datetime import date, timedelta

def saturdays_between_two_dates(start_date, end_date):
    saturdays_count = 0

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    while start_date <= end_date:
        if start_date.weekday() == 5:
            saturdays_count += 1
        start_date += timedelta(days=1)

    return saturdays_count


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))