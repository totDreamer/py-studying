from datetime import date, timedelta

def get_all_mondays(year):
    d = date(int(year), 1, 1)
    days_untill = (0 - d.weekday()) % 7
    first_monday =  d + timedelta(days=days_untill)

    all_mondays = []
    today = first_monday
    while today.year == d.year:
        all_mondays.append(today)
        today += timedelta(days=7)

    return all_mondays

print(get_all_mondays(input()))