from datetime import datetime, timedelta

h, m, s = map(int, input().split(':'))
delta_time = timedelta(hours=h, minutes=m, seconds=s)

print(int(delta_time.total_seconds()))