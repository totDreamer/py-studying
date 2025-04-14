from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
start = datetime.strptime(input(), pattern) - timedelta(days=1)
for i in range(1, 11):
    start = start + timedelta(days=i)
    print(start.strftime(pattern))