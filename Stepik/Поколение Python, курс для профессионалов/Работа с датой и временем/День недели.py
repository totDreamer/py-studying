from datetime import datetime
from calendar import day_name

day = datetime.strptime(input(), '%Y-%m-%d')
print(day_name[day.weekday()])