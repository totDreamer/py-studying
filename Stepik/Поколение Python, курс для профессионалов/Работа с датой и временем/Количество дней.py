from calendar import monthrange

year, m = map(int, input().split())
print(monthrange(year, m)[1])