from calendar import monthrange, month_name

year, m = input().split()
year, m = int(year), list(month_name).index(m)
print(monthrange(year, m)[1])