from datetime import datetime, timedelta

start_time = datetime.strptime(input(), '%H:%M:%S')
p_sec = timedelta(seconds=int(input()))
delta_time = (start_time + p_sec).strftime('%H:%M:%S')

print(delta_time)