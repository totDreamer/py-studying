from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
def fill_up_missing_dates(dates):
    dates = [datetime.strptime(d, pattern) for d in dates]
    full_dates = []

    start = min(dates)
    end = max(dates)
    while start != end + timedelta(days=1):
        full_dates.append(start.strftime(pattern))
        start += timedelta(days=1)

    return full_dates


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))