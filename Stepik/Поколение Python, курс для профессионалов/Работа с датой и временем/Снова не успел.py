from datetime import datetime, timedelta

weekday_open = {i: 9 if i < 5 else 10 for i in range(7)}
weekday_close = {i: 21*60 if i < 5 else 18*60 for i in range(7)}

def time_until_closing(d):
    d = datetime.strptime(d, '%d.%m.%Y %H:%M')
    if weekday_open[d.weekday()] <= d.hour < weekday_close[d.weekday()]//60:
        result = weekday_close[d.weekday()] - d.hour * 60 - d.minute
    else:
        result = 'Магазин не работает'

    return result

print(time_until_closing(input()))