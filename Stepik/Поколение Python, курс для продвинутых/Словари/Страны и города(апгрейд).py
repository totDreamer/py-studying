city_country_dict = {}

for _ in range(int(input())):
    string = input().split()
    city_country_dict[string[0]] = string[1:]

for _ in range(int(input())):
    new_city = input()
    for key, values in city_country_dict.items():
        if new_city in values:
            print(key)