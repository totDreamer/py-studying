from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

pattern = '%H:%M'
total_min = 0

def spended_time(times):
    start = datetime.strptime(times[0], pattern)
    end = datetime.strptime(times[1], pattern)
    total_sec = (end-start).total_seconds()
    return (total_sec//60)

for d in data:
    total_min += int(spended_time(d))

print(total_min)