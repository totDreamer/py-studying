n = int(input())
city_set = set([input() for city in range(n)])
last_city = input()
if last_city in city_set:
    print('REPEAT')
else:
    print('OK')