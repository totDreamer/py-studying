import calendar


year, m = input().split()
year, m = int(year), list(calendar.month_abbr).index(m)
calendar.prmonth(year, m)