from datetime import datetime, timedelta

start_date = datetime.strptime(input(), '%d.%m.%Y')
minus_day = (start_date - timedelta(days=1)).strftime('%d.%m.%Y')
plus_day = (start_date + timedelta(days=1)).strftime('%d.%m.%Y')

print(minus_day, plus_day, sep='\n')