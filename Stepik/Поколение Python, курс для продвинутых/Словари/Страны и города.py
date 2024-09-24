n = int(input())
city_country_dict = {}
for _ in range(n):
    string = input().split()
    country, cities = string[0], string[1:]
    city_country_dict[country] = cities
m = int(input())
new_cities = []
for _ in range(m):
    new_city = input()
    new_cities.append(new_city)
for city in new_cities:
    for key, values in city_country_dict.items():
        if city in values:
            print(key)